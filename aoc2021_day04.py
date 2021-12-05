"""
    Advent of Code 2021
    Day 04: Giant Squid
"""

import pytest


class Board:
    def __init__(self, lst):
        self.rows = [[int(x) for x in row] for row in lst]
        self.num_cols = len(lst[0])

    def cross_out(self, n):
        for row in self.rows:
            for i, _ in enumerate(row):
                if row[i] == n:
                    row[i] = None
                    return True
        return False

    def is_winner(self):
        has_winning_row = any(all(x is None for x in row) for row in self.rows)
        has_winning_col = any(
            all(row[i] is None for row in self.rows) for i in range(self.num_cols)
        )
        return has_winning_row or has_winning_col

    def score(self):
        return sum(sum(x for x in row if x is not None) for row in self.rows)


def win_score_gen(draw_data, boards_data):
    boards = [Board(b) for b in boards_data]
    num_boards = len(boards)
    draw = [int(x) for x in reversed(draw_data)]
    winners = set()
    while draw and len(winners) < num_boards:
        n = draw.pop()
        for b_idx, board in enumerate(boards):
            if b_idx in winners:
                continue
            if board.cross_out(n) and board.is_winner():
                winners.add(b_idx)
                yield board.score() * n


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        lines = data_file.read().splitlines()
    draw_data = lines[0].split(",")
    boards_data = []
    for line in lines[1:]:
        if line == "":
            boards_data.append([])
        else:
            boards_data[-1].append(line.split())
    return draw_data, boards_data


def day04_part01(score_gen):
    return next(score_gen)


def day04_part02(score_gen):
    return list(score_gen)[-1]


@pytest.fixture(autouse=True, name="score_gen")
def fixture_score_gen():
    # Setup tests from puzzle description
    draw_data, boards_data = parse_input("data/day04_test.txt")
    return win_score_gen(draw_data, boards_data)


def test_day04_part01(score_gen):
    assert day04_part01(score_gen) == 188 * 24  # 4512


def test_day04_part02(score_gen):
    assert day04_part02(score_gen) == 148 * 13  # 1924


if __name__ == "__main__":
    bingo = win_score_gen(*parse_input("data/day04.txt"))

    # Part 1
    print("What will your final score be if you choose that board?")
    print(day04_part01(bingo))  # Correct answer is 58412

    # Part 2
    print(
        "Figure out which board will win last. Once it wins, what would its final score be?"
    )
    print(day04_part02(bingo))  # Correct answer is 10030
