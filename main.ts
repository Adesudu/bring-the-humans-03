/**
 * Entrypoint: bring-the-humans-03 make.fun bounty entry.
 * Copies VIDEO.json from BOT directory to OUTPUT directory.
 * Owner: Adesudu, Referral code: qq4pkark.
 * Video: ad.mp4 (720x1280, 18s), posted on TikTok from @adewijayanto07.
 */
import { copyFileSync, mkdirSync } from 'node:fs';
import { resolve, join } from 'node:path';

const botDir = process.env.MAKEFUN_BOT_DIR || '.';
const outputDir = process.env.MAKEFUN_OUTPUT_DIR || '/output';

mkdirSync(outputDir, { recursive: true });
const src = resolve(botDir, 'VIDEO.json');
const dest = join(outputDir, 'VIDEO.json');

copyFileSync(src, dest);
console.log(`Copied ${src} to ${dest}`);
