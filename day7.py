from collections import defaultdict

data = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".strip()

with open("./resources/day7.txt") as f:
    data = f.read().strip()

splitters = set()
start_beam = None
lines = data.split("\n")
end_row = len(lines)

for row, line in enumerate(lines):
    for col, val in enumerate(line):
        if val == 'S':
            start_beam = (row, col)
        elif val == '^':
            splitters.add((row, col))

split_points = set()
current_beams = set()
cache = defaultdict(lambda: 0)


def move_beam(beam):
    if beam in cache:
        return cache[beam]

    row, col = beam
    if row == end_row:
        return 1

    paths = 0
    if (row, col) in splitters:
        split_points.add((row, col))
        paths += move_beam((row + 1, col - 1))
        paths += move_beam((row + 1, col + 1))
    else:
        paths = move_beam((row + 1, col))

    cache[beam] = paths
    return paths

total = move_beam(start_beam)


def part1():
    print(len(split_points))


def part2():
    print(total)

part1()
part2()
