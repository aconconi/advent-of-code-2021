"""
    Advent of Code 2021
    Day 07: The Treachery of Whales
"""

from math import ceil, floor
from statistics import mean, median

import pytest


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        return [int(x) for x in data_file.read().split(",")]


def day07_part1(data):
    med = int(median(data))
    return sum(abs(x - med) for x in data)


def day07_part2(data):
    def gauss_sum(n):
        return n * (n + 1) // 2

    avg = mean(data)
    avg_floor, avg_ceil = floor(avg), ceil(avg)
    return min(
        [
            sum(gauss_sum(abs(x - avg_floor)) for x in data),
            sum(gauss_sum(abs(x - avg_ceil)) for x in data),
        ]
    )


@pytest.fixture(autouse=True, name="test_data")
def fixture_test_data():
    return parse_input("data/day07_test.txt")


def test_day07_part1(test_data):
    assert day07_part1(test_data) == 37


def test_day07_part2(test_data):
    assert day07_part2(test_data) == 168


if __name__ == "__main__":
    input_data = parse_input("data/day07.txt")

    print("Day 07 Part 1:")
    print(day07_part1(input_data))  # Correct answer is 351901

    print("Day 07 Part 2:")
    print(day07_part2(input_data))  # Correct answer is 101079875
