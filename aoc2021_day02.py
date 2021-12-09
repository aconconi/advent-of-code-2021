"""
    Advent of Code 2021
    Day 02: Dive!
"""

import pytest


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        input_data = []
        for line in data_file.readlines():
            command, value = line.split()
            input_data.append((command, int(value)))
        return input_data


def day02_part01(data):
    hpos = 0
    depth = 0
    for cmd, val in data:
        if cmd == "forward":
            hpos += val
        else:
            depth += val if cmd == "down" else -val
    return hpos * depth


def day02_part02(data):
    hpos = 0
    depth = 0
    aim = 0
    for cmd, val in data:
        if cmd == "forward":
            hpos += val
            depth += aim * val
        else:
            aim += val if cmd == "down" else -val
    return hpos * depth


@pytest.fixture(autouse=True, name="test_data")
def fixture_test_data():
    return parse_input("data/day02_test.txt")


def test_day02_part1(test_data):
    assert day02_part01(test_data) == 150


def test_day02_part2(test_data):
    assert day02_part02(test_data) == 900


if __name__ == "__main__":
    input_data = parse_input("data/day02.txt")

    print("Day 02 Part 1:")
    print(day02_part01(input_data))  # Correct answer is 1451208

    print("Day 02 Part 2:")
    print(day02_part02(input_data))  # Correct answer is 1620141160
