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

def get_paper_positions():
    paper_positions = set()
    for row, line in enumerate(data.strip().split("\n")):
        for column, char in enumerate(line):
            if char == "@":
                paper_positions.add((row, column))

    return paper_positions


def find_rolls_to_remove(paper_positions):
    removed = set()
    for (row, column) in paper_positions:
        adj = 0
        for r, c in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            if (row + r, column + c) in paper_positions:
                adj += 1

        if adj < 4:
            removed.add((row, column))

    return removed


def part1():
    removed = find_rolls_to_remove(get_paper_positions())
    print(len(removed))


def part2():
    total = 0
    paper_positions = get_paper_positions()
    while True:
        removed = find_rolls_to_remove(paper_positions)
        if len(removed) == 0:
            break

        total += len(removed)
        paper_positions = paper_positions - removed

    print(total)


part1()
part2()
