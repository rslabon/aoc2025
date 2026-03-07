data = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

with open("./resources/day5.txt") as f:
    data = f.read()

part1, part2 = data.strip().split("\n\n")
ranges = []
for line in part1.strip().split("\n"):
    start, end = line.split("-")
    start, end = int(start), int(end)
    ranges.append((start, end))

ranges = list(sorted(ranges, key=lambda x: (x[0], x[1])))

ids = [int(id) for id in part2.strip().split("\n")]


def part1():
    fresh = 0
    for id in ids:
        for (start, end) in ranges:
            if start <= id <= end:
                fresh += 1
                break

    print(fresh)


part1()
