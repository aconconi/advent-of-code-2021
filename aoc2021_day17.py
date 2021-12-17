"""
    Advent of Code 2021
    Day 17: Trick Shot
"""

from itertools import product
from re import findall
from math import comb

import pytest


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        return parse_target_line(data_file.readline())


def parse_target_line(line):
    return [int(a) for a in findall(r"-?\d+", line)]


def day17_part1(target):
    _, _, y1, y2 = target
    return comb(abs(min(y1, y2)), 2)


def day17_part2(target):
    x1, x2, y1, y2 = target
    count = 0
    for vx, vy in product(range(x2 + 1), range(y1, x2 + 1)):
        x, y = 0, 0
        while x <= x2 and (vy > 0 or y >= y1) and (vx > 0 or x >= x1):
            x += vx
            y += vy
            vx -= vx // abs(vx) if vx else 0
            vy -= 1
            if x1 <= x <= x2 and y1 <= y <= y2:
                count += 1
                break
    return count


@pytest.fixture(autouse=True, name="test_data")
def fixture_test_data():
    return parse_target_line("target area: x=20..30, y=-10..-5")


def test_day17_part1(test_data):
    assert day17_part1(test_data) == 45


def test_day17_part2(test_data):
    assert day17_part2(test_data) == 112


if __name__ == "__main__":
    input_data = parse_input("data/day17.txt")

    print("Day 17 Part 1:")
    print(day17_part1(input_data))  # Correct answer is 3916

    print("Day 17 Part 2:")
    print(day17_part2(input_data))  # Correct answer is 2986
