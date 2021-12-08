"""
    Advent of Code 2021
    Day 08: Seven Segment Search
"""

from itertools import permutations

import pytest


LETTERS = "abcdefg"
UNIQUE_LENGHTS = [2, 3, 4, 7]
RENDER = {
    s: str(i)
    for i, s in enumerate(
        "abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg".split()
    )
}


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        lines = data_file.read().splitlines()
        data = []
        for line in lines:
            pattern, out_val = line.split("|")
            pattern = ["".join(sorted(x)) for x in pattern.split()]
            out_val = ["".join(sorted(x)) for x in out_val.split()]
            data.append((pattern, out_val))
        return data


def day08_part01(data):
    return sum(
        sum(len(v) in UNIQUE_LENGHTS for v in outval)
        for _, outval in data
    )


def is_solution(pattern, perm):
    trans = str.maketrans(perm, LETTERS)
    a = set("".join(sorted(c.translate(trans))) for c in pattern)
    return a == set(RENDER.keys())


def solve(pattern):
    return next(
        "".join(perm)
        for perm in permutations(LETTERS)
        if is_solution(pattern, "".join(perm))
    )


def day08_part02(data):
    # Brute forcing on segments (arguably the worst approach, there are smarter way to solve this!)
    total = 0
    for pattern, outval in data:
        trans = str.maketrans(solve(pattern), LETTERS)
        decode = "".join(RENDER["".join(sorted(v.translate(trans)))] for v in outval)
        total += int(decode)
    return total


@pytest.fixture(autouse=True, name="test_data")
def fixture_test_data():
    return parse_input("data/day08_test.txt")


def test_day08_part01(test_data):
    assert day08_part01(test_data) == 26


def test_day08_part02(test_data):
    assert day08_part02(test_data) == 61229


if __name__ == "__main__":
    input_data = parse_input("data/day08.txt")

    # Part 1
    print("Day 08 Part 1:")
    print(day08_part01(input_data))  # Correct answer is 532

    # Part 2
    print("Day 08 Part 2:")
    print(day08_part02(input_data))  # Correct answer is 1011284
