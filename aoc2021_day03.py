"""
    Advent of Code 2021
    Day 03: Binary Diagnostic
"""

import operator

import pytest


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        return data_file.read().splitlines()


def day03_part1(data):
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


def day03_part2(data):
    return solve_set(data, operator.ge) * solve_set(data, operator.lt)


@pytest.fixture(autouse=True, name="test_data")
def fixture_test_data():
    return parse_input("data/day03_test.txt")


def test_day03_part1(test_data):
    assert day03_part1(test_data) == 198  # 22 * 9


def test_day03_part2(test_data):
    assert day03_part2(test_data) == 230  # 23 * 10


if __name__ == "__main__":
    input_data = parse_input("data/day03.txt")

    print("Day 03 Part 1:")
    print(day03_part1(input_data))  # Correct answer is 3895776

    print("Day 03 Part 2:")
    print(day03_part2(input_data))  # Correct answer is 7928162
