"""
    Advent of Code 2021
    Day 09: Smoke Basin
"""


import pytest


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        return data_file.read().splitlines()


def neighbors(heigth, width, pos):
    i, j = pos
    return set(
        p2
        for p2 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        if 0 <= p2[0] < heigth and 0 <= p2[1] < width
    )


def low_points(data):
    heigth, width = len(data), len(data[0])
    return [
        (i, j)
        for i, row in enumerate(data)
        for j, c in enumerate(row)
        if all(data[i2][j2] > c for i2, j2 in neighbors(heigth, width, (i, j)))
    ]


def basin_size(data, pos):
    heigth, width = len(data), len(data[0])
    stack = [pos]
    seen = set()
    while stack:
        v = stack.pop()
        if v in seen:
            continue
        seen.add(v)
        i, j = v
        stack.extend(
            (i2, j2)
            for i2, j2 in neighbors(heigth, width, v)
            if data[i][j] < data[i2][j2] < "9"
        )
    return len(seen)


def day09_part01(data):
    return sum(int(data[i][j]) + 1 for i, j in low_points(data))


def day09_part02(data):
    sizes = sorted(
        [basin_size(data, low_point) for low_point in low_points(data)], reverse=True
    )
    return sizes[0] * sizes[1] * sizes[2]


@pytest.fixture(autouse=True, name="test_data")
def fixture_test_data():
    return parse_input("data/day09_test.txt")


def test_day09_part01(test_data):
    assert day09_part01(test_data) == 15


def test_day09_part02(test_data):
    assert day09_part02(test_data) == 1134


if __name__ == "__main__":
    input_data = parse_input("data/day09.txt")

    print("Day 09 Part 1:")
    print(day09_part01(input_data))  # Correct answer is 585

    print("Day 09 Part 2:")
    print(day09_part02(input_data))  # Correct answer is 827904
