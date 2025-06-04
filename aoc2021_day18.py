"""
Advent of Code 2021
Day 18: Snailfish
"""

from functools import reduce

import pytest

SnailfishNumber = int | tuple["SnailfishNumber", "SnailfishNumber"]


def parse_input(file_path: str) -> list[SnailfishNumber]:
    with open(file_path, encoding="ascii") as f:
        return [eval(line) for line in f.read().splitlines()]


def add_to_side(sn: SnailfishNumber, value: int, to_left: bool) -> SnailfishNumber:
    if isinstance(sn, int):
        return sn + value
    left, right = sn
    return (
        (add_to_side(left, value, True), right)
        if to_left
        else (left, add_to_side(right, value, False))
    )


def explode(
    sn: SnailfishNumber, depth: int = 1
) -> tuple[bool, int, SnailfishNumber, int]:
    if isinstance(sn, int):
        return False, 0, sn, 0

    left, right = sn
    if depth > 4 and isinstance(left, int) and isinstance(right, int):
        return True, left, 0, right

    exploded, carry_l, new_left, carry_r = explode(left, depth + 1)
    if exploded:
        return True, carry_l, (new_left, add_to_side(right, carry_r, True)), 0

    exploded, carry_l, new_right, carry_r = explode(right, depth + 1)
    if exploded:
        return True, 0, (add_to_side(left, carry_l, False), new_right), carry_r

    return False, 0, sn, 0


def split(sn: SnailfishNumber) -> tuple[bool, SnailfishNumber]:
    if isinstance(sn, int):
        return (True, (sn // 2, sn - sn // 2)) if sn >= 10 else (False, sn)

    left, right = sn
    left_did_split, new_left = split(left)
    if left_did_split:
        return True, (new_left, right)

    right_did_split, new_right = split(right)
    return right_did_split, (left, new_right)


def add_snailfish(a: SnailfishNumber, b: SnailfishNumber) -> SnailfishNumber:
    result = (a, b)
    did_split = True
    while did_split:
        exploded, _, result, _ = explode(result)
        if not exploded:
            did_split, result = split(result)
    return result


def magnitude(sn: SnailfishNumber) -> int:
    return sn if isinstance(sn, int) else 3 * magnitude(sn[0]) + 2 * magnitude(sn[1])


def day18_part1(numbers: list[SnailfishNumber]) -> int:
    return magnitude(reduce(add_snailfish, numbers))


def day18_part2(numbers: list[SnailfishNumber]) -> int:
    return max(
        magnitude(add_snailfish(a, b))
        for i, a in enumerate(numbers)
        for j, b in enumerate(numbers)
        if i != j
    )


@pytest.fixture(autouse=True, name="test_data")
def fixture_test_data() -> list[SnailfishNumber]:
    return parse_input("data/day18_test.txt")


def test_part1(test_data: list[SnailfishNumber]) -> None:
    assert day18_part1(test_data) == 4140


def test_part2(test_data: list[SnailfishNumber]) -> None:
    assert day18_part2(test_data) == 3993


if __name__ == "__main__":
    input_data = parse_input("data/day18.txt")

    print("Day 18 Part 1:")
    print(day18_part1(input_data))  # Correct answer is 4365

    print("Day 18 Part 2:")
    print(day18_part2(input_data))  # Correct answer is 4490
