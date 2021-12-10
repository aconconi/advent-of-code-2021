"""
    Advent of Code 2021
    Day 08: Seven Segment Search
"""

from collections import Counter
from itertools import permutations

import pytest


DIGITS = "abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg"
LETTERS = "abcdefg"
UNIQUE_LENGHTS = [2, 3, 4, 7]
RENDER = {s: str(i) for i, s in enumerate(DIGITS.split())}


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        lines = data_file.read().splitlines()
        data = []
        for line in lines:
            pattern, out_val = line.split("|")
            data.append((pattern.split(), out_val.split()))
        return data


def day08_part1(data):
    return sum(sum(len(v) in UNIQUE_LENGHTS for v in outval) for _, outval in data)


def day08_part2_brute_force(data):
    # Brute force testing 2^7 permutations: not the most efficient approach

    def decode(s, trans):
        return "".join(sorted(s.translate(trans)))

    total = 0
    for pattern, outval in data:
        for perm in permutations(LETTERS):
            trans = str.maketrans("".join(perm), LETTERS)
            decoded_pattern = [decode(p, trans) for p in pattern]
            if all(x in RENDER.keys() for x in decoded_pattern):
                decoded_outval = "".join(RENDER[decode(v, trans)] for v in outval)
                total += int(decoded_outval)
    return total


def day08_part2(data):
    # More efficient approach: cracking the code with frequency analysis

    # Find frequencies of segments in clear representation
    c = Counter(DIGITS.replace(" ", ""))
    freq = {
        tuple(sorted(c[x] for x in digit)): str(i)
        for i, digit in enumerate(DIGITS.split())
    }

    # Decode each output value analyzing segment frequencies in signals pattern
    total = 0
    for pattern, outval in data:
        c = Counter("".join(pattern))
        total += int("".join(freq[tuple(sorted(c[x] for x in v))] for v in outval))
    return total


@pytest.fixture(autouse=True, name="test_data")
def fixture_test_data():
    return parse_input("data/day08_test.txt")


def test_day08_part1(test_data):
    assert day08_part1(test_data) == 26


def test_day08_part2(test_data):
    assert day08_part2(test_data) == 61229


if __name__ == "__main__":
    input_data = parse_input("data/day08.txt")

    print("Day 08 Part 1:")
    print(day08_part1(input_data))  # Correct answer is 532

    print("Day 08 Part 2:")
    print(day08_part2(input_data))  # Correct answer is 1011284
