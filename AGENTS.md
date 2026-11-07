# Agent Guidelines for Advent of Code 2026

## Strict Isolation of Solution Sources

When implementing or modifying solutions in `src/solutions/gemini/`:

1. **Do Not Inspect Hand-Crafted Solutions**:
   - Never read, inspect, or reference any files in `src/solutions/by_hand/`.
   - Treat `src/solutions/by_hand/` as strictly off-limits.
   - When searching the codebase (e.g. via `grep`, file search, or terminal commands), scope searches explicitly to `src/solutions/gemini/`, `src/lib/`, or `inputs/`, or exclude `src/solutions/by_hand/`.
   - If any snippet from `src/solutions/by_hand/` appears in tool output, ignore it completely.

2. **Permitted Information Sources**:
   - Puzzle descriptions: `inputs/day{XX}puzzle.txt` (or text provided directly in the prompt).
   - Puzzle inputs: `inputs/day{XX}.txt` and `inputs/day{XX}example.txt`.
   - Shared library utilities: `src/lib/` (e.g., `Grid2D`, `Point2D`, `Point3D`, `Direction`, `types`).
   - The target solution file: `src/solutions/gemini/day{XX}.py`.

## Solution Structure & Interface Contract

Each solution module (`src/solutions/gemini/day{XX}.py`) must implement three functions:

1. `prepare_input(file_content: list[str]) -> PuzzleInput`:
   - Receives the raw input file content as a list of strings (lines stripped of trailing `\n`).
   - Parses and transforms the raw lines into appropriate data structures for the puzzle.

2. `part1(input: PuzzleInput) -> None`:
   - Must include an **extensive commentary docstring** right at the beginning of the function explaining:
     - The objective and logic of Part 1.
     - The algorithmic approach, data structures, and mathematical reasoning used.
     - Why this solution works for the puzzle and how edge cases are handled.
   - Solves Part 1 of the puzzle.
   - Must **print** the calculated answer to stdout (the runner does not print return values).

3. `part2(input: PuzzleInput) -> None`:
   - Must include an **extensive commentary docstring** right at the beginning of the function explaining:
     - How Part 2 modifies or expands upon Part 1.
     - Any new algorithmic complexities, optimizations, or data structures introduced (e.g., scaling, cycle detection, dynamic programming).
     - Why this solution works for the puzzle.
   - Solves Part 2 of the puzzle.
   - Must **print** the calculated answer to stdout.

## Solution Workflow & Verification

When asked to solve a puzzle:
1. Read the puzzle description from `inputs/day{XX}puzzle.txt` (or user prompt) and review the example inputs in `inputs/day{XX}example.txt`.
2. Implement `prepare_input`, `part1`, and `part2` in `src/solutions/gemini/day{XX}.py`, including the detailed docstrings explaining the methodology.
3. Verify the solution against the example input first:
   ```shell
   uv run solve {XX} -g -e
   ```
4. Run the solution with the full input:
   ```shell
   uv run solve {XX} -g
   ```
5. **Mandatory Linting Step**:
   - After writing or modifying any solution, run `./lint.sh`.
   - Fix any formatting or linting issues flagged by Ruff until the command exits cleanly.
