"""
    Advent of Code 2021
    Day 14: Extended Polymerization
"""

from collections import Counter, defaultdict

import pytest


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        template, rules = data_file.read().split("\n\n")
        rules = {(rule[0], rule[1]): rule[-1] for rule in rules.splitlines()}
        return template, rules


def solve(template, rules, num_steps):
    # count initial pairs 
    current_count = Counter(zip(template, template[1:]))

    for _ in range(num_steps):
        # on each iteration update the count
        new_count = defaultdict(int)
        for pair in current_count:
            if pair in rules:
                # if there is a rule AB->X, then AB pairs
                # generate new AX and XB pairs and disappear
                a, b = pair
                new_count[a, rules[pair]] += current_count[pair]
                new_count[rules[pair], b] += current_count[pair]
            else:
                # no rule for this pair, just leave it
                new_count[pair] = current_count[pair]
        current_count = new_count

    # count total occurrencies of each letter as second letter in the pairs
    letters_count = defaultdict(int)
    for a, b in current_count:
        letters_count[b] += current_count[a, b]
    return max(letters_count.values()) - min(letters_count.values())


def day14_part1(data):
    template, rules = data
    return solve(template, rules, 10)


def day14_part2(data):
    template, rules = data
    return solve(template, rules, 40)


@pytest.fixture(autouse=True, name="test_data")
def fixture_test_data():
    return parse_input("data/day14_test.txt")


def test_day14_part1(test_data):
    assert day14_part1(test_data) == 1588


def test_day14_part2(test_data):
    assert day14_part2(test_data) == 2188189693529


if __name__ == "__main__":
    input_data = parse_input("data/day14.txt")

    print("Day 14 Part 1:")
    print(day14_part1(input_data))  # Correct answer is 3230

    print("Day 14 Part 2:")
    print(day14_part2(input_data))  # Correct answer is 3542388214529
