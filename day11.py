from collections import deque

data = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

data = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""

with open("./resources/day11.txt") as f:
    data = f.read().strip()


class Node:
    def __init__(self, id):
        self.id = id
        self.children = set()

    def add_node(self, other):
        self.children.add(other)

    def __repr__(self) -> str:
        return f"{self.id}"


lines = []
nodes = {}
rnodes = {}

for line in data.strip().split("\n"):
    id, others = line.split(":")
    others = others.strip().split(" ")
    lines.append((id, tuple(others)))
    if id not in nodes:
        nodes[id] = Node(id)
        rnodes[id] = Node(id)
    for other in others:
        if other not in nodes:
            nodes[other] = Node(other)
            rnodes[other] = Node(other)

        rnodes[other].children.add(rnodes[id])
        nodes[id].children.add(nodes[other])

cache = {}


def count_paths(from_id, to_id, path=[]):
    if from_id == to_id:
        return 1

    if from_id in path:
        return 0

    if (from_id, to_id) in cache:
        return cache[(from_id, to_id)]

    node = nodes[from_id]

    c = 0
    for other in node.children:
        c += count_paths(other.id, to_id, path + [from_id])

    cache[(from_id, to_id)] = c

    return c


def part1():
    start = nodes["you"]
    end = nodes["out"]
    q = deque([(start, [])])
    path_count = 0
    while q:
        node, path = q.popleft()

        if node in path:
            continue

        if node == end:
            path += [node]
            path_count += 1
            continue

        for other in node.children:
            q.append((other, path + [node]))

    print(path_count)


def part2():
    global cache

    cache = {}
    svr_fft = count_paths("svr", "fft")

    cache = {}
    dac_out = count_paths("dac", "out")

    cache = {}
    fft_dac = count_paths("fft", "dac")
    cache = {}

    print(svr_fft * fft_dac * dac_out)


part1()
part2()
