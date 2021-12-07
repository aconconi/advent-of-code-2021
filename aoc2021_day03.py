"""
    Advent of Code 2021
    Day 03: Binary Diagnostic
"""

import operator

import pytest


def day03_part01(data):
    ones = [0] * len(data[0])
    for digits in data:
        for i, d in enumerate(digits):
            ones[i] += 1 if d == "1" else -1
    gamma = int("".join(str(int(x >= 0)) for x in ones), 2)
    epsilon = int("".join(str(int(x < 0)) for x in ones), 2)
    return gamma * epsilon


def solve_set(data, comparison_op):
    a = set(data)
    for i in range(len(data[0])):
        selector = (
            "1"
            if comparison_op(sum(entry[i] == "1" for entry in a), len(a) / 2)
            else "0"
        )
        a = {entry for entry in a if entry[i] == selector}
        if len(a) == 1:
            return int(a.pop(), 2)
    return None


def day03_part02(data):
    return solve_set(data, operator.ge) * solve_set(data, operator.lt)


@pytest.fixture(name="test_data")
def fixture_test_data():
    return ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]


def test_day03_part1(test_data):
    assert day03_part01(test_data) == 22 * 9


def test_day03_part2(test_data):
    assert day03_part02(test_data) == 23 * 10


if __name__ == "__main__":
    with open("data/day03.txt", "r", encoding="ascii") as data_file:
        input_data = data_file.read().splitlines()

    # Part 1
    print("What is the power consumption of the submarine?")
    print(day03_part01(input_data))  # Correct answer is 3895776

    # Part 2
    print("What is the life support rating of the submarine?")
    print(day03_part02(input_data))  # Correct answer is 7928162
