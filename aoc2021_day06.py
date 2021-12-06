"""
    Advent of Code 2021
    Day 06: Lanternfish
"""

from collections import deque
import pytest


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        z = data_file.readlines()[0]
        return [int(x) for x in z.split(",")]


def smart_add(a, x):
    if x is None:
        return a
    elif a is None:
        return x
    else:
        return a + x


def solve(data, days):
    c = [None] * 9
    for x in data:
        c[x] = smart_add(c[x], 1)
    c = deque(c)
    for _ in range(days):
        c.rotate(-1)
        c[6] = smart_add(c[6], c[8])
    return sum(x for x in c if x is not None)


def day06_part01(data):
    return solve(data, 80)


def day06_part02(data):
    return solve(data, 256)


@pytest.fixture(autouse=True, name="test_data")
def fixture_test_data():
    return parse_input("data/day06_test.txt")


def test_day06_part01(test_data):
    assert day06_part01(test_data) == 5934


def test_day06_part02(test_data):
    assert day06_part02(test_data) == 26984457539


if __name__ == "__main__":
    input_data = parse_input("data/day06.txt")

    # Part 1
    print("Day 06 Part 1:")
    print(day06_part01(input_data))  # Correct answer is 362639

    # Part 2
    print("Day 06 Part 2:")
    print(day06_part02(input_data))  # Correct answer is 1639854996917
