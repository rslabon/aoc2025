import shapely
from shapely.geometry import Polygon

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


def read_points():
    points = []
    for line in data.strip().split("\n"):
        x, y = line.split(",")
        points.append((int(x), int(y)))

    return points


def area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    width = abs(x1 - x2) + 1
    height = abs(y1 - y2) + 1
    return width * height


def part1():
    max_area = float("-inf")
    points = read_points()
    for i, point in enumerate(points):
        j = i + 1
        while j < len(points):
            other_point = points[j]
            max_area = max(max_area, area(point, other_point))
            j += 1

    print(max_area)


def part2():
    points = read_points()
    boundry = Polygon(points).normalize()

    max_area = float("-inf")
    for i, p1 in enumerate(points):
        j = i + 1
        while j < len(points):
            p2 = points[j]
            p3 = (p2[0], p1[1])
            p4 = (p1[0], p2[1])

            rectangle = Polygon([p1, p2, p3, p4]).convex_hull
            if shapely.covered_by(rectangle, boundry):
                max_area = max(max_area, area(p1, p2))

            j += 1

    print(max_area)


part1()
part2()
