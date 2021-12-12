"""
    Advent of Code 2021
    Day 12: Passage Pathing
"""

from collections import defaultdict

import pytest


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        graph = defaultdict(set)
        for line in data_file.read().splitlines():
            a, b = line.split("-")
            graph[a].add(b)
            graph[b].add(a)
        return graph


def gen_paths(graph, allow_single_small_twice=False):
    stack = [(["start"], False)]
    while stack:
        path, twice = stack.pop()
        if path[-1] == "end":
            yield path
            continue
        for neigh in graph[path[-1]]:
            if neigh not in path or neigh.isupper():
                stack.append((path + [neigh], twice))
            elif (
                allow_single_small_twice
                and not twice
                and neigh.islower()
                and neigh not in ["start", "end"]
            ):
                stack.append((path + [neigh], True))


def day12_part1(graph):
    return sum(1 for _ in gen_paths(graph))


def day12_part2(graph):
    return sum(1 for _ in gen_paths(graph, allow_single_small_twice=True))


@pytest.fixture(autouse=True, name="test_data")
def fixture_test_data():
    return [parse_input(f"data/day12_test{i}.txt") for i in [1, 2, 3]]


def test_day12_part1(test_data):
    assert day12_part1(test_data[0]) == 10
    assert day12_part1(test_data[1]) == 19
    assert day12_part1(test_data[2]) == 226


def test_day12_part2(test_data):
    assert day12_part2(test_data[0]) == 36
    assert day12_part2(test_data[1]) == 103
    assert day12_part2(test_data[2]) == 3509


if __name__ == "__main__":
    input_data = parse_input("data/day12.txt")

    print("Day 12 Part 1:")
    print(day12_part1(input_data))  # Correct answer is 5457

    print("Day 12 Part 2:")
    print(day12_part2(input_data))  # Correct answer is 128506
