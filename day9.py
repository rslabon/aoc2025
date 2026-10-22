data = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

with open("./resources/day9.txt") as f:
    data = f.read().strip()

points = []
for line in data.strip().split("\n"):
    x, y = line.split(",")
    points.append((int(x), int(y)))


def area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    width = abs(x1 - x2) + 1
    height = abs(y1 - y2) + 1
    return width * height


def part1():
    max_area = float("-inf")
    for i, point in enumerate(points):
        j = i + 1
        while j < len(points):
            other_point = points[j]
            max_area = max(max_area, area(point, other_point))
            j += 1

    print(max_area)


part1()
