"""
    Advent of Code 2021
    Day 04: Giant Squid
"""

import copy


def is_winning_board(board):
    if any(row == [None, None, None, None, None] for row in board) or any(
        all(row[i] == None for row in board) for i in range(len(board[0]))
    ):
        return sum(sum(x for x in row if x is not None) for row in board)
    return False


def win_score_gen(draw, input_boards):
    boards = copy.deepcopy(input_boards)
    winners = set()
    for n in draw:
        if len(winners) == len(boards):
            return
        for b_idx, board in enumerate(boards):
            if b_idx in winners:
                continue
            for row in board:
                for i, _ in enumerate(row):
                    if row[i] == n:
                        row[i] = None
                        break
            s = is_winning_board(board)
            if s != False:
                winners.add(b_idx)
                yield s * n


def day04_part01(draw, boards):
    return next(win_score_gen(draw, boards))


def day04_part02(draw, boards):
    return list(win_score_gen(draw, boards))[-1]


def test_day04():
    draw, boards = parse_input("data/day04_test.txt")
    assert day04_part01(draw, boards) == 188 * 24  # 4512
    assert day04_part02(draw, boards) == 148 * 13  # 1924


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        lines = data_file.read().splitlines()
    draw = [int(x) for x in lines.pop(0).split(",")]
    boards = []
    for line in lines:
        if line == "":
            boards.append([])
        else:
            boards[-1].append([int(x) for x in line.split()])
    return draw, boards


if __name__ == "__main__":
    draw, boards = parse_input("data/day04.txt")

    # Part 1
    print("What will your final score be if you choose that board?")
    print(day04_part01(draw, boards))  # Correct answer is 58412

    # Part 2
    print(
        "Figure out which board will win last. Once it wins, what would its final score be?"
    )
    print(day04_part02(draw, boards))  # Correct answer is
