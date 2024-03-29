"""
    Advent of Code 2021
    Day 11: Dumbo Octopus
"""

from itertools import count

import pytest

DELTA = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        return data_file.read().splitlines()


def build_grid(data):
    """Builds a dictionary representation of the input grid."""
    return {(i, j): int(c) for i, row in enumerate(data) for j, c in enumerate(row)}


def neighbors(pos):
    i, j = pos
    for di, dj in DELTA:
        if 0 <= i + di < 10 and 0 <= j + dj < 10:
            yield (i + di, j + dj)


def tick(grid):
    """Evolves grid and returns number of flashes occurred during this step."""

    flashes = 0

    # First, the energy level of each octopus increases by 1.
    charged = set()
    for p in grid:
        grid[p] += 1
        if grid[p] > 9:
            charged.add(p)

    # Then, any octopus with energy level greater than 9
    # flashes and triggers a chain reaction.
    while charged:
        p = charged.pop()
        flashes += 1
        grid[p] = 0
        for p2 in filter(lambda x: grid[x] > 0, neighbors(p)):
            grid[p2] += 1
            if grid[p2] > 9:
                charged.add(p2)

    return flashes


def day11_part1(data):
    grid = build_grid(data)
    return sum(tick(grid) for _ in range(100))


def day11_part2(data):
    grid = build_grid(data)
    return next(step for step in count(1) if tick(grid) == 100)


@pytest.fixture(autouse=True, name="test_data")
def fixture_test_data():
    return parse_input("data/day11_test.txt")


def test_day11_part1(test_data):
    assert day11_part1(test_data) == 1656


def test_day11_part2(test_data):
    assert day11_part2(test_data) == 195


if __name__ == "__main__":
    input_data = parse_input("data/day11.txt")

    print("Day 11 Part 1:")
    print(day11_part1(input_data))  # Correct answer is 1757

    print("Day 11 Part 2:")
    print(day11_part2(input_data))  # Correct answer is 422
