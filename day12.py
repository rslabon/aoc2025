data = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""

with open("./resources/day12.txt") as f:
    data = f.read()

blocks = data.strip().split("\n\n")
block1 = blocks[:-1]
block2 = blocks[-1]

shapes = {}
for line in block1:
    id, shape_block = line.split(":")
    cells = 0
    for row in shape_block.strip().split("\n"):
        cells += sum([1 if cell == "#" else 0 for cell in row])

    shapes[int(id)] = cells

regions = []
for line in block2.split("\n"):
    size, quantity = line.split(":")
    width, height = size.split("x")
    width, height = int(width), int(height)
    quantity = quantity.strip().split(" ")
    quantity = [int(q) for q in quantity]
    regions.append((width, height, quantity))

total = len(regions)
for i, (width, height, quantity) in enumerate(regions):
    whole_area = width * height
    required_area = 0
    for i, q in enumerate(quantity):
        required_area += shapes[i] * q

    if required_area > whole_area:
        total -= 1

print(total)
