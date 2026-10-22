from collections import Counter
from functools import reduce
from math import sqrt

data = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

with open("./resources/day8.txt") as f:
    data = f.read().strip()

boxes = set()


class UnionFind:
    def __init__(self, elements):
        self.id = {e: e for e in elements}
        self.size = {e: 1 for e in elements}

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]

        return p

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return

        if self.size[p_root] < self.size[q_root]:
            self.id[p_root] = q_root
            self.size[q_root] += self.size[p_root]
            del self.size[p_root]
        else:
            self.id[q_root] = p_root
            self.size[p_root] += self.size[q_root]
            del self.size[q_root]


for line in data.split("\n"):
    if line.strip():
        x, y, z = line.split(",")
        boxes.add((int(x), int(y), int(z)))


def distance(a, b):
    return sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2) + pow(a[2] - b[2], 2))


def find_closest():
    closest = set()
    zero = (0, 0, 0)
    for box in boxes:
        remining_boxes = boxes - {box}
        for b in remining_boxes:
            if distance(box, zero) < distance(b, zero):
                closest.add((distance(box, b), box, b))
            else:
                closest.add((distance(box, b), b, box))

    closest = list(sorted(closest, key=lambda x: x[0]))
    return closest


def part1():
    closest = find_closest()
    uf = UnionFind(boxes)

    for _, box, other_box in closest[0:1000]:
        if uf.is_connected(box, other_box):
            continue

        uf.union(box, other_box)

    counter = Counter(uf.size.values())
    biggest = list(sorted(counter.items(), key=lambda i: i[0], reverse=True))
    biggest = [b[0] for b in biggest[0:3]]
    total = reduce(lambda a, b: a * b, biggest, 1)
    print(total)


def part2():
    closest = find_closest()
    uf = UnionFind(boxes)

    for _, box, other_box in closest:
        if uf.is_connected(box, other_box):
            continue

        uf.union(box, other_box)
        counter = Counter(uf.size.values())
        if len(counter.items()) == 1:
            print(box[0] * other_box[0])
            break


part1()
part2()
