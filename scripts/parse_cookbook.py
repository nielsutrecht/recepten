#!/usr/bin/env python3
"""
Parse high-protein.txt cookbook into individual recipe markdown files.

Usage: python3 parse_cookbook.py [input.txt] [output-dir]
"""

import re
import os
import sys
from pathlib import Path

INPUT = sys.argv[1] if len(sys.argv) > 1 else str(Path.home() / "Downloads/high-protein.txt")
OUTPUT_DIR = sys.argv[2] if len(sys.argv) > 2 else str(Path.home() / "src/project/recepten/input")

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(INPUT, "r", encoding="utf-8") as f:
    text = f.read()

# Split into chapter sections first, then into recipe blocks within each section.
# Chapter headers appear as form-feed lines like "\x0cBREAKFAST." or "\x0cLunch."
CHAPTER_RE = re.compile(r"\x0c(BREAKFAST|LUNCH|DINNER|SNACKS?|DESSERTS?|SIDES?)\.?\s*\n", re.IGNORECASE)
chapter_parts = CHAPTER_RE.split(text)
# chapter_parts = [pre-chapter text, name1, body1, name2, body2, ...]
# Build list of (section_name, body_text) pairs; prepend a None section for front matter.
chapter_chunks = [("none", chapter_parts[0])]
for i in range(1, len(chapter_parts), 2):
    name = chapter_parts[i].strip().lower().rstrip("s")  # "breakfast","lunch","dinner","snack"
    body = chapter_parts[i + 1] if i + 1 < len(chapter_parts) else ""
    chapter_chunks.append((name, body))

# Flatten into (section, block) pairs split by Panacea Palm within each chapter
section_blocks = []
for section, body in chapter_chunks:
    for block in re.split(r"\n\x0c?Panacea Palm\n", "\n" + body):
        section_blocks.append((section, block))


def slugify(s):
    s = s.lower()
    s = re.sub(r"[''']", "", s)
    s = re.sub(r"[^a-z0-9\s-]", " ", s)
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"-+", "-", s)
    return s[:70].rstrip("-")


def parse_nutrition(text):
    result = {}
    for key, pat in [
        ("calories", r"calories\s*[-–]\s*(\d+)\s*kcal"),
        ("protein",  r"protein\s*[-–]\s*(\d+)\s*g"),
        ("carbs",    r"carbs?\s*[-–]\s*(\d+)\s*g"),
        ("fat",      r"fat\s*[-–]\s*(\d+)\s*g"),
        ("servings", r"serv(?:ings?)?\s*[-–]\s*(\S+)"),
    ]:
        m = re.search(pat, text, re.IGNORECASE)
        result[key] = m.group(1) if m else "?"
    return result


INSTR_VERBS = re.compile(
    r"^(heat|cook|add|mix|combine|place|pour|bake|grill|fry|stir|whisk|blend|"
    r"season|serve|prepare|bring|remove|crack|preheat|spread|drizzle|top|fold|"
    r"roll|slice|dice|chop|cut|once|in a |to a |for the |start|spray|toss|"
    r"transfer|simmer|boil|roast|marinate|layer|assemble|divide|set aside|"
    r"rinse|make|let |turn|fill|brush|cover|sprinkle|melt|toast|repeat|allow|"
    r"spoon|drain|squeeze|flatten|lightly|meanwhile|carefully|now |using|get |"
    r"while|when |after |next |then )",
    re.IGNORECASE,
)

# Prose markers — commas + connectives suggest a sentence, not an ingredient
PROSE = re.compile(r",\s|\b(until|then|into|once|and cook|and mix|and stir|and allow|to allow)\b", re.IGNORECASE)


def looks_like_instruction(line):
    """Detect the start of the instruction block."""
    if len(line) < 45 or re.match(r"^[-\d½¼¾]", line):
        return False
    verb_match = bool(INSTR_VERBS.match(line))
    prose_match = bool(PROSE.search(line))
    # Long line with a verb, or any line that reads like a prose sentence
    return (verb_match and len(line) > 55) or (verb_match and prose_match) or (len(line) > 95 and prose_match)


def parse_recipe(block):
    lines = block.split("\n")

    # --- Title: everything before the NUtrition header ---
    title_lines = []
    for line in lines:
        if re.match(r"^NUtrition\b", line.strip(), re.IGNORECASE):
            break
        stripped = line.strip()
        if stripped and not re.match(r"^\d+$", stripped):
            title_lines.append(stripped)

    if not title_lines:
        return None

    title = " ".join(title_lines).strip()

    # Skip chapter dividers and front-matter sections
    if re.match(r"^(BREAKFAST|LUNCH|DINNER|SNACKS?|DESSERTS?|SIDES?|THE\s|CLICK\s)", title, re.IGNORECASE):
        return None

    # --- Must have an INGREDIENTS section ---
    ingr_idx = block.upper().find("\nINGREDIENTS")
    if ingr_idx < 0:
        return None

    # Nutrition lives between title and INGREDIENTS
    nutr = parse_nutrition(block[:ingr_idx + 150])

    # --- Body: everything after INGREDIENTS ---
    body = block[ingr_idx:].lstrip()
    body = re.sub(r"^INGREDIENTS\s*\n", "", body, flags=re.IGNORECASE)
    body_lines = body.split("\n")

    # Join wrapped ingredient lines: if a line doesn't end with punctuation and the
    # next line is short and doesn't start a new ingredient, merge them.
    joined = []
    k = 0
    while k < len(body_lines):
        line = body_lines[k].strip()
        while (
            k + 1 < len(body_lines)
            and line
            and not line.endswith((":", ",", ".", "!", "?"))
            and not re.match(r"^[-\d½¼¾]", body_lines[k + 1].strip())
            and not re.match(r"^(Notes?|INGREDIENTS)\s*$", body_lines[k + 1].strip(), re.IGNORECASE)
            and not looks_like_instruction(body_lines[k + 1].strip())
            and 0 < len(body_lines[k + 1].strip()) < 25
        ):
            k += 1
            line = line + " " + body_lines[k].strip()
        joined.append(line)
        k += 1
    body_lines = joined

    ingredients = []
    notes_lines = []
    instr_start = None
    in_notes = False

    for j, raw in enumerate(body_lines):
        line = raw.strip()

        # Notes section header
        if re.match(r"^Notes?\s*$", line, re.IGNORECASE):
            in_notes = True
            continue

        if in_notes:
            # Exit notes when we hit an instruction line
            if looks_like_instruction(line):
                instr_start = j
                break
            # Exit notes on a blank line followed by instruction
            if not line:
                # peek ahead
                rest = "\n".join(body_lines[j+1:]).strip()
                first_next = rest.split("\n")[0].strip() if rest else ""
                if looks_like_instruction(first_next):
                    instr_start = j + 1 + body_lines[j+1:].index(first_next.split("\n")[0])
                    break
            if line:
                notes_lines.append(line)
            continue

        # Detect instruction start: a long prose line
        if looks_like_instruction(line):
            instr_start = j
            break

        # Otherwise it's an ingredient line
        if line:
            ingredients.append(line)

    # --- Instructions: join remaining lines into paragraphs ---
    if instr_start is not None:
        instr_text = "\n".join(body_lines[instr_start:]).strip()
    else:
        instr_text = ""

    # Split into paragraphs (blank-line separated)
    paragraphs = []
    for para in re.split(r"\n\s*\n", instr_text):
        para = re.sub(r"\s+", " ", para.replace("\n", " ")).strip()
        if para:
            paragraphs.append(para)

    notes = re.sub(r"\s+", " ", " ".join(notes_lines)).strip()

    return {
        "title": title,
        "nutrition": nutr,
        "ingredients": ingredients,
        "instructions": paragraphs,
        "notes": notes,
    }


def is_subsection_header(line):
    """Short lines with no quantity that look like sub-section headers within ingredients."""
    return (
        not re.match(r"^[-\d½¼¾]", line)
        and len(line) < 45
        and not re.search(r"\d", line)
        and line == line.strip()
        and len(line.split()) <= 5
    )


def detect_section(block):
    """Return a normalised section name if this block is a chapter header, else None."""
    text = re.sub(r"[\x0c\s]", " ", block).strip().rstrip(".")
    SECTIONS = {
        "breakfast": "breakfast",
        "lunch": "lunch",
        "dinner": "dinner",
        "snacks": "snacks",
        "snack": "snacks",
        "dessert": "desserts",
        "desserts": "desserts",
        "sides": "sides",
    }
    lower = text.lower()
    if lower in SECTIONS and len(text) < 20:
        return SECTIONS[lower]
    return None


def format_markdown(r):
    n = r["nutrition"]
    section_line = f"Section: {r['section']}" if r.get("section") else ""
    lines = [
        f"# {r['title']}",
        "",
        f"Servings: {n['servings']} | "
        f"Calories: {n['calories']}kcal | "
        f"Protein: {n['protein']}g | "
        f"Carbs: {n['carbs']}g | "
        f"Fat: {n['fat']}g",
    ]
    if section_line:
        lines.append(section_line)
    lines += [
        "",
        "## Ingredients",
        "",
    ]

    for ing in r["ingredients"]:
        if not ing:
            continue
        if is_subsection_header(ing):
            lines += ["", f"**{ing}**", ""]
        else:
            ing = re.sub(r"^-\s*", "", ing)
            lines.append(f"- {ing}")

    if r["notes"]:
        lines += ["", "## Notes", "", r["notes"]]

    lines += ["", "## Instructions", ""]

    if r["instructions"]:
        for i, para in enumerate(r["instructions"], 1):
            lines.append(f"{i}. {para}")
            lines.append("")
    else:
        lines.append("*(instructions not extracted — check source)*")

    return "\n".join(lines)


# --- Main loop ---
count = 0
skipped = 0
seen = {}

for section, block in section_blocks:
    block = block.strip()

    if len(block) < 100:
        skipped += 1
        continue

    recipe = parse_recipe(block)
    if not recipe:
        skipped += 1
        continue

    recipe["section"] = None if section == "none" else section

    if not recipe["ingredients"] and not recipe["instructions"]:
        skipped += 1
        continue

    slug = slugify(recipe["title"])
    if not slug:
        skipped += 1
        continue

    # Deduplicate filenames
    if slug in seen:
        seen[slug] += 1
        slug = f"{slug}-{seen[slug]}"
    else:
        seen[slug] = 1

    md = format_markdown(recipe)
    out_path = os.path.join(OUTPUT_DIR, f"{slug}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md)

    count += 1
    print(f"  {slug}.md")

print(f"\nDone: {count} recipes → {OUTPUT_DIR}/")
print(f"Skipped {skipped} non-recipe blocks.")
