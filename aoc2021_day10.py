"""
    Advent of Code 2021
    Day 10: Syntax Scoring
"""

from functools import reduce
from statistics import median

import pytest


MATCH = {"(": ")", "[": "]", "{": "}", "<": ">"}
SCORE = {")": (3, 1), "]": (57, 2), "}": (1197, 3), ">": (25137, 4)}


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        return data_file.read().splitlines()


def corruption(line):
    """Returns corruption score and rest of the stack"""
    stack = []
    for c in line:
        if c in MATCH:
            stack.append(c)
            continue
        if not stack or MATCH[stack.pop()] != c:
            return SCORE[c][0], stack
    return 0, stack


def day10_part1(data):
    return sum(corruption(line)[0] for line in data)


def day10_part2(data):
    scores = []
    for line in data:
        cs, stack = corruption(line)
        if not cs:
            scores.append(
                reduce(lambda s, x: s * 5 + SCORE[MATCH[x]][1], reversed(stack), 0)
            )
    return int(median(scores))


@pytest.fixture(autouse=True, name="test_data")
def fixture_test_data():
    return parse_input("data/day10_test.txt")


def test_day10_part1(test_data):
    assert day10_part1(test_data) == 26397


def test_day10_part2(test_data):
    assert day10_part2(test_data) == 288957


if __name__ == "__main__":
    input_data = parse_input("data/day10.txt")

    print("Day 10 Part 1:")
    print(day10_part1(input_data))  # Correct answer is 318099

    print("Day 10 Part 2:")
    print(day10_part2(input_data))  # Correct answer is 2389738699
