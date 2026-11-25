import { copyFileSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// Copies the front-page image for Wednesday 25 November 2026 into the
// grader's output directory, byte for byte, every run.
const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const src = join(here, "entry.png");
const dst = join(outDir, "entry.png");

mkdirSync(outDir, { recursive: true });
copyFileSync(src, dst);

// The grader runs this program twice and both runs must write the same
// bytes: fail loudly instead of silently leaving a partial copy behind.
if (statSync(src).size !== statSync(dst).size) {
  throw new Error("entry.png copy is incomplete");
}
