"""
    Advent of Code 2021
    Day 10: Syntax Scoring
"""

from functools import reduce
from statistics import median

import pytest

SCORE1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
SCORE2 = {")": 1, "]": 2, "}": 3, ">": 4}
MATCH = {"(": ")", "[": "]", "{": "}", "<": ">"}


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        return data_file.read().splitlines()


def corruption_score(line):
    stack = []
    for c in line:
        if c in MATCH:
            stack.append(c)
            continue
        if not stack or MATCH[stack.pop()] != c:
            return SCORE1[c], stack
    return 0, stack


def day10_part01(data):
    return sum(corruption_score(line)[0] for line in data)


def day10_part02(data):
    scores = []
    for line in data:
        cs, stack = corruption_score(line)
        if not cs:
            scores.append(
                reduce(lambda s, x: s * 5 + SCORE2[MATCH[x]], reversed(stack), 0)
            )
    return int(median(scores))


@pytest.fixture(autouse=True, name="test_data")
def fixture_test_data():
    return parse_input("data/day10_test.txt")


def test_day10_part01(test_data):
    assert day10_part01(test_data) == 26397


def test_day10_part02(test_data):
    assert day10_part02(test_data) == 288957


if __name__ == "__main__":
    input_data = parse_input("data/day10.txt")

    print("Day 10 Part 1:")
    print(day10_part01(input_data))  # Correct answer is 318099

    print("Day 10 Part 2:")
    print(day10_part02(input_data))  # Correct answer is 2389738699
