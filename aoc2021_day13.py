"""
    Advent of Code 2021
    Day 13: Transparent Origami
"""

import pytest


def parse_input(file_name):
    """Returns a tuple (dots, instructions) where dots is a set of (x, y) coordinates
    and instructions is a list of (axis_index, fold_line_index) pairs.
    """
    with open(file_name, "r", encoding="ascii") as data_file:
        dots, instructions = data_file.read().split("\n\n")
        dots = set(tuple(int(k) for k in pair.split(",")) for pair in dots.splitlines())
        instructions = [
            ("xy".index(line[11]), int(line[13:])) for line in instructions.splitlines()
        ]
        return dots, instructions


def fold(points, instruction):
    axis, fold_line = instruction
    new_points = set()
    for point in points:
        p = list(point)
        if p[axis] == fold_line:
            # points on the fold line disappear
            continue
        if p[axis] > fold_line:
            # points below the fold line are flipped around that
            p[axis] = 2 * fold_line - p[axis]
        new_points.add(tuple(p))
    return new_points


def dots_to_string(dots):
    width = max(x for x, _ in dots) + 1
    height = max(y for _, y in dots) + 1
    return "\n".join(
        "".join("#" if (x, y) in dots else "." for x in range(width))
        for y in range(height)
    )


def day13_part1(data):
    dots, instructions = data
    return len(fold(dots, instructions[0]))


def day13_part2(data):
    dots, instructions = data
    for instruction in instructions:
        dots = fold(dots, instruction)
    return dots_to_string(dots)


@pytest.fixture(autouse=True, name="test_data")
def fixture_test_data():
    return parse_input("data/day13_test.txt")


def test_day13_part1(test_data):
    assert day13_part1(test_data) == 17


def test_day13_pytepart2(test_data):
    assert day13_part2(test_data) == "#####\n#...#\n#...#\n#...#\n#####"


if __name__ == "__main__":
    input_data = parse_input("data/day13.txt")

    print("Day 13 Part 1:")
    print(day13_part1(input_data))  # Correct answer is 942

    print("Day 13 Part 2:")
    print(day13_part2(input_data))  # Correct answer is JZGUAPRB
