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

for line in data.strip().split("\n"):
    id, others = line.split(":")
    others = others.strip().split(" ")
    lines.append((id, tuple(others)))
    if id not in nodes:
        node = Node(id)
        nodes[id] = node
    for other in others:
        if other not in nodes:
            nodes[other] = Node(other)
        nodes[id].children.add(nodes[other])


def part1():
    start = nodes["you"]
    end = nodes["out"]
    q = deque([(start, [])])
    path_count = 0
    while q:
        node, visited = q.popleft()

        if node in visited:
            continue

        if node == end:
            visited += [node]
            path_count += 1
            continue

        for other in node.children:
            q.append((other, visited + [node]))

    print(path_count)


part1()
