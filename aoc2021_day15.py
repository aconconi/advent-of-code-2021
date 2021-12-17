"""
    Advent of Code 2021
    Day 15: Chiton
"""

import heapq

import pytest


def parse_input(file_name):
    with open(file_name, "r", encoding="ascii") as data_file:
        return data_file.read().splitlines()


class RiskGrid:
    def __init__(self, data, repeat=1):
        self.height = len(data)
        self.width = len(data[0])
        self.height_repeated = self.height * repeat
        self.width_repeated = self.width * repeat
        self.grid = {
            (i, j): int(data[i][j])
            for i in range(self.height)
            for j in range(self.width)
        }

    def neighbors(self, pos):
        x, y = pos
        for dx, dy in [(0, -1), (0, +1), (-1, 0), (+1, 0)]:
            x2, y2 = x + dx, y + dy
            if 0 <= x2 < self.width_repeated and 0 <= y2 < self.height_repeated:
                yield x2, y2

    def cost(self, pos):
        x, y = pos
        inc_x, gx = divmod(x, self.width)
        inc_y, gy = divmod(y, self.height)
        return (self.grid[gx, gy] - 1 + inc_x + inc_y) % 9 + 1

    def find_shortest_path(self):
        source = (0, 0)
        destination = self.width_repeated - 1, self.height_repeated - 1

        # Dijkstra shortest path algorithm with priority queue.
        visited = set()
        queue = [(0, source)]
        while queue:
            distance, pos = heapq.heappop(queue)
            if pos == destination:
                return distance
            if pos in visited:
                continue
            visited.add(pos)
            for neigh in self.neighbors(pos):
                if neigh not in visited:
                    heapq.heappush(queue, (distance + self.cost(neigh), neigh))
        # queue empty, no path found
        return None


def day15_part1(data):
    return RiskGrid(data).find_shortest_path()


def day15_part2(data):
    return RiskGrid(data, repeat=5).find_shortest_path()


@pytest.fixture(autouse=True, name="test_data")
def fixture_test_data():
    return parse_input("data/day15_test.txt")


def test_day15_part1(test_data):
    assert day15_part1(test_data) == 40


def test_day15_part2(test_data):
    assert day15_part2(test_data) == 315


if __name__ == "__main__":
    input_data = parse_input("data/day15.txt")

    print("Day 15 Part 1:")
    print(day15_part1(input_data))  # Correct answer is 553

    print("Day 15 Part 2:")
    print(day15_part2(input_data))  # Correct answer is 2858
