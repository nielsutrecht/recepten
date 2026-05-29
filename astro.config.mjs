import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://nielsutrecht.github.io',
  base: '/recepten',
  integrations: [sitemap()],
});
