"""
    Advent of Code 2021
    Day 01: Sonar Sweep
"""

import pytest


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        return [int(x) for x in data_file.readlines()]


def day01_part01(data):
    return sum(current > prev for prev, current in zip(data, data[1:]))


def day01_part02(data):
    triads = [sum(t) for t in zip(data, data[1:], data[2:])]
    return day01_part01(triads)


@pytest.fixture(autouse=True, name="test_data")
def fixture_test_data():
    return parse_input("data/day01_test.txt")


def test_day01_part1(test_data):
    assert day01_part01(test_data) == 7


def test_day01_part2(test_data):
    assert day01_part02(test_data) == 5


if __name__ == "__main__":
    input_data = parse_input("data/day01.txt")

    print("Day 01 Part 1:")
    print(day01_part01(input_data))  # Correct answer is 1446

    print("Day 01 Part 2:")
    print(day01_part02(input_data))  # Correct answer is 1486
