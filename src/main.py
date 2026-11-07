import argparse
import importlib
import time
from pathlib import Path


def run_solve(day: int, example: bool, gemini: bool = False) -> None:
    day_str = f"day{int(day):02d}"
    example_file = "example" if example else ""
    input_file = Path("inputs") / f"{day_str}{example_file}.txt"

    submodule = "gemini" if gemini else "by_hand"
    module_name = f"solutions.{submodule}.{day_str}"
    day_module = importlib.import_module(module_name)
    prepare_input = day_module.prepare_input
    part1 = day_module.part1
    part2 = day_module.part2

    print(f"Performing solve for Day {day}...")

    print()
    print("Starting Part 1...")
    with input_file.open("r") as f:
        p1_data = prepare_input([line.strip("\n") for line in f.readlines()])
    p1_start = time.perf_counter()
    part1(p1_data)
    p1_time_ms = (time.perf_counter() - p1_start) * 1000
    print(f"Part 1 completed in {p1_time_ms:.3f} ms")

    print()
    print("Starting Part 2...")
    with input_file.open("r") as f:
        p2_data = prepare_input([line.strip("\n") for line in f.readlines()])
    p2_start = time.perf_counter()
    part2(p2_data)
    p2_time_ms = (time.perf_counter() - p2_start) * 1000
    print(f"Part 2 completed in {p2_time_ms:.3f} ms")


def solve():
    parser = argparse.ArgumentParser(
        description="Run a solution for a given Advent of Code day."
    )
    parser.add_argument("day", type=int, help="Day number to run (e.g. 1)")
    parser.add_argument(
        "-e", "--example", action="store_true", help="Use the example input file"
    )
    parser.add_argument(
        "-g",
        "--gemini",
        action="store_true",
        help="Use Gemini solution instead of manually solved solution",
    )

    args = parser.parse_args()

    run_solve(args.day, args.example, args.gemini)


if __name__ == "__main__":
    solve()
