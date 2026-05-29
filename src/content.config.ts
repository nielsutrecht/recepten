import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const ratingEmoji = z.enum(['😍', '😊', '😐', '😒', '🤢']);

const ingredientCategory = z.enum([
  'groente en fruit',
  'vlees en vis',
  'zuivel en eieren',
  'kaas',
  'pasta en granen',
  'sauzen en kruiden',
  'conserven',
  'bakken',
  'overig',
]);

const recipes = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/recipes' }),
  schema: z.object({
    title: z.string(),
    pubDate: z.coerce.date(),
    servings: z.number().int().positive(),
    prepTime: z.number().int().positive(),
    cookTime: z.number().int().positive().optional(),
    tags: z.array(z.string()).default([]),
    source: z.string().optional(),
    ratings: z
      .object({
        emma: ratingEmoji,
        annemijn: ratingEmoji,
      })
      .partial()
      .optional(),
    draft: z.boolean().default(false),
    ingredients: z.array(
      z.object({
        quantity: z.number().positive(),
        unit: z.string(),
        name: z.string(),
        category: ingredientCategory.optional(),
      })
    ),
  }),
});

export const collections = { recipes };
