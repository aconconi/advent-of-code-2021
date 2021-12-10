"""
    Advent of Code 2021
    Day 04: Giant Squid
"""

import pytest


def is_winner(board, seen):
    num_cols = len(board[0])
    has_winning_row = any(all(x in seen for x in row) for row in board)
    has_winning_col = any(all(row[i] in seen for row in board) for i in range(num_cols))
    return has_winning_row or has_winning_col


def score(board, seen):
    return sum(sum(set(row) - seen) for row in board)


def win_score_gen(draw_data, boards):
    draw = list(reversed(draw_data))
    num_boards = len(boards)
    winners = set()
    seen = set()
    while draw and len(winners) < num_boards:
        n = draw.pop()
        seen.add(n)
        for b_idx, board in enumerate(boards):
            if b_idx in winners:
                continue
            if is_winner(board, seen):
                winners.add(b_idx)
                yield score(board, seen) * n


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        lines = data_file.read().splitlines()
    draw_data = tuple(int(x) for x in lines[0].split(","))
    boards_data = []
    for line in lines[1:]:
        if line == "":
            boards_data.append([])
        else:
            boards_data[-1].append([int(x) for x in line.split()])
    return draw_data, boards_data


def day04_part1(score_gen):
    return next(score_gen)


def day04_part2(score_gen):
    return list(score_gen)[-1]


@pytest.fixture(autouse=True, name="score_gen")
def fixture_score_gen():
    # Setup tests from puzzle description
    draw_data, boards_data = parse_input("data/day04_test.txt")
    return win_score_gen(draw_data, boards_data)


def test_day04_part1(score_gen):
    assert day04_part1(score_gen) == 188 * 24  # 4512


def test_day04_part2(score_gen):
    assert day04_part2(score_gen) == 148 * 13  # 1924


if __name__ == "__main__":
    bingo = win_score_gen(*parse_input("data/day04.txt"))

    print("Day 04 Part 1:")
    print(day04_part1(bingo))  # Correct answer is 58412

    print("Day 04 Part 2:")
    print(day04_part2(bingo))  # Correct answer is 10030
