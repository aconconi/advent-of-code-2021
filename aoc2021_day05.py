"""
    Advent of Code 2021
    Day 05: Hydrothermal Venture
"""

import re
import pytest
from collections import Counter


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        m = re.findall(r"(\d+),(\d+)\s\-\>\s(\d+),(\d+)", data_file.read())
    return [((int(x1), int(y1)), (int(x2), int(y2))) for x1, y1, x2, y2 in m]


def line_points(line):
    (x1, y1), (x2, y2) = line
    if x1 == x2:
        return ((x1, y) for y in range(y1, y2 + 1))
    elif y1 == y2:
        return ((x, y1) for x in range(x1, x2 + 1))


def diag_points(line):
    (x1, y1), (x2, y2) = line
    dx = 1 if x2 > x1 else -1
    dy = 1 if y2 > y1 else -1
    x = x1
    y = y1
    while min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
        yield (x, y)
        x += dx
        y += dy


def day05_part01(data):
    lines = [
        tuple(sorted(((x1, y1), (x2, y2))))
        for ((x1, y1), (x2, y2)) in data
        if x1 == x2 or y1 == y2
    ]
    c = Counter()
    for line in lines:
        c.update(line_points(line))
    return sum(c[point] > 1 for point in c)


def day05_part02(data):
    lines = [
        tuple(sorted(((x1, y1), (x2, y2))))
        for ((x1, y1), (x2, y2)) in data
        if x1 == x2 or y1 == y2
    ]
    diagonals = [
        tuple(sorted(((x1, y1), (x2, y2))))
        for ((x1, y1), (x2, y2)) in data
        if abs(x2 - x1) == abs(y2 - y1)
    ]
    c = Counter()
    for line in lines:
        c.update(line_points(line))
    for line in diagonals:
        c.update(diag_points(line))
    return sum(c[point] > 1 for point in c)


@pytest.fixture(autouse=True)
def test_data():
    return parse_input("data/day05_test.txt")


def test_day05_part01(test_data):
    assert day05_part01(test_data) == 5


def test_day05_part01(test_data):
    assert day05_part02(test_data) == 12


if __name__ == "__main__":
    input_data = parse_input("data/day05.txt")

    # Part 1
    print("Day 05 Part 1:")
    print(day05_part01(input_data))  # Correct answer is 6311

    # Part 2
    print("Day 05 Part 2:")
    print(day05_part02(input_data))  # Correct answer is 19929
