"""
    Advent of Code 2021
    Day 02: Dive!
"""


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


def test_day02():
    test_data = [
        ("forward", 5),
        ("down", 5),
        ("forward", 8),
        ("up", 3),
        ("down", 8),
        ("forward", 2),
    ]
    assert day02_part01(test_data) == 150
    assert day02_part02(test_data) == 900


if __name__ == "__main__":
    with open("data/day02.txt", "r", encoding="ascii") as data_file:
        lines = data_file.readlines()
        input_data = []
        for line in lines:
            cmd, val = line.split()
            input_data.append((cmd, int(val)))

    # Part 1
    print(
        "What do you get if you multiply your final horizontal position by your final depth?"
    )
    print(day02_part01(input_data))  # Correct answer is 1451208

    # Part 2
    print(
        "What do you get if you multiply your final horizontal position by your final depth?"
    )
    print(day02_part02(input_data))  # Correct answer is 1620141160
