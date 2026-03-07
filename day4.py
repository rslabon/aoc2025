data = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

with open("./resources/day4.txt") as f:
    data = f.read()

paper_positions = set()
max_row = 0
max_column = 0
for row, line in enumerate(data.strip().split("\n")):
    max_row = max(max_row, row)
    for column, char in enumerate(line):
        max_column = max(max_column, column)
        if char == "@":
            paper_positions.add((row, column))


def part1():
    rolls = 0
    for (row, column) in paper_positions:
        adj = 0
        for r, c in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            if (row + r, column + c) in paper_positions:
                adj += 1

        if adj < 4:
            rolls += 1

    print(rolls)


part1()
