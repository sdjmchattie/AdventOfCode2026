# Advent of Code 2026 Solutions in Python

Solutions to Advent of Code 2026 written in Python.

## Running Solutions

To run the solution for a day, first ensure you have the `uv` tool installed, then run the command:

```shell
uv run solve 1
```

This solves day 1 with the inputs I was given on Advent of Code. Change the number to the day you want to solve.

### Command-Line Options and Flags

```text
usage: solve [-h] [-e] [-g] day
```

| Argument / Flag | Shorthand | Description                                                                                  |
| --------------- | --------- | -------------------------------------------------------------------------------------------- |
| `day`           |           | Day number to run (e.g. `1`, `2`).                                                           |
| `--example`     | `-e`      | Use the example input file (`inputs/day{XX}example.txt`) instead of the puzzle input.        |
| `--gemini`      | `-g`      | Use the `solutions.gemini` sub-module instead of the default `solutions.by_hand` sub-module. |
| `--help`        | `-h`      | Show the help message and exit.                                                              |

#### Usage Examples

```shell
# Solve Day 1 with standard input using by-hand solution
uv run solve 1

# Solve Day 1 with example input
uv run solve 1 -e

# Solve Day 1 using Gemini solution
uv run solve 1 --gemini

# Solve Day 1 using Gemini solution with example input
uv run solve 1 -e -g
```

## Project Structure

- `src/solutions/by_hand/`: Hand-crafted solutions.
- `src/solutions/gemini/`: Gemini-generated solutions.
- `src/lib/`: Shared utilities and helpers (e.g., `Grid2D`, `Point2D`, `Point3D`, `Direction`).
- `inputs/`: Inputs for each day (`day{XX}.txt` for puzzle inputs, `day{XX}example.txt` for examples, and `day{XX}puzzle.txt` for puzzle text).

## Code Style & Linting

Run formatting and linting with:

```shell
./lint.sh
```

## Commentary

If you want to follow along my commentary of how these solutions work, please check out my blog series on [Advent of Code solutions](https://stuart.mchattie.net/tags/advent-of-code/).
