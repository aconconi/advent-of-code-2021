"""
    Advent of Code 2021
    Day 05: Hydrothermal Venture
"""

import re
from collections import Counter
from dataclasses import dataclass

import pytest


@dataclass(frozen=True)
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    def is_horizontal(self):
        return self.y1 == self.y2

    def is_vertical(self):
        return self.x1 == self.x2

    def is_diagonal(self):
        return abs(self.x2 - self.x1) == abs(self.y2 - self.y1)

    @staticmethod
    def delta(a, b):
        return 0 if a == b else (b - a) // abs(b - a)

    def points(self):
        dx, dy = Line.delta(self.x1, self.x2), Line.delta(self.y1, self.y2)
        min_x, max_x = min(self.x1, self.x2), max(self.x1, self.x2)
        min_y, max_y = min(self.y1, self.y2), max(self.y1, self.y2)
        x, y = self.x1, self.y1
        while min_x <= x <= max_x and min_y <= y <= max_y:
            yield (x, y)
            x += dx
            y += dy


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        m = re.findall(r"(\d+),(\d+)\s\-\>\s(\d+),(\d+)", data_file.read())
    return [Line(int(x1), int(y1), int(x2), int(y2)) for x1, y1, x2, y2 in m]


def day05_part1(lines):
    c = Counter()
    for line in lines:
        if line.is_horizontal() or line.is_vertical():
            c.update(line.points())
    return sum(c[point] > 1 for point in c)


def day05_part2(lines):
    c = Counter()
    for line in lines:
        if line.is_diagonal() or line.is_horizontal() or line.is_vertical():
            c.update(line.points())
    return sum(c[point] > 1 for point in c)


@pytest.fixture(autouse=True, name="test_data")
def fixture_test_data():
    return parse_input("data/day05_test.txt")


def test_day05_part1(test_data):
    assert day05_part1(test_data) == 5


def test_day05_part2(test_data):
    assert day05_part2(test_data) == 12


if __name__ == "__main__":
    input_data = parse_input("data/day05.txt")

    print("Day 05 Part 1:")
    print(day05_part1(input_data))  # Correct answer is 6311

    print("Day 05 Part 2:")
    print(day05_part2(input_data))  # Correct answer is 19929
