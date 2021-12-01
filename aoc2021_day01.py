"""
    Advent of Code 2021
    Day 01: Sonar Sweep
"""


def day01_part01(data):
    return sum(current > prev for prev, current in zip(data, data[1:]))


def day01_part02(data):
    triads = [sum(t) for t in zip(data, data[1:], data[2:])]
    return day01_part01(triads)


def test_day01():
    test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert day01_part01(test_data) == 7
    assert day01_part02(test_data) == 5


if __name__ == "__main__":
    # Read input file into lines
    with open("data/day01.txt", "r", encoding="ascii") as data_file:
        lines = data_file.readlines()
        input_data = [int(x) for x in lines]

    # Part 1
    print("How many measurements are larger than the previous measurement?")
    print(day01_part01(input_data))  # Correct answer is 1446

    # Part 2
    print("How many sums are larger than the previous sum?")
    print(day01_part02(input_data))  # Correct answer is 1486
