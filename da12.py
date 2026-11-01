import copy
from functools import cache
from typing import Any

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

blocks = data.strip().split("\n\n")
block1 = blocks[:-1]
block2 = blocks[-1]

shapes = []
for line in block1:
    _, shape_block = line.split(":")
    shape = []
    for row in shape_block.strip().split("\n"):
        shape.append([1 if cell == "#" else 0 for cell in row])

    shapes.append(shape)

regions = []
for line in block2.split("\n"):
    size, quantity = line.split(":")
    width, height = size.split("x")
    width, height = int(width), int(height)
    quantity = quantity.strip().split(" ")
    quantity = [int(q) for q in quantity]
    regions.append((width, height, quantity))


def create_region(width, height):
    rows = []
    for ridx in range(height):
        row = list([0] * width)
        rows.append(row)

    return rows


def put_shape(region, shape, dr=0, dc=0):
    for ridx, row in enumerate(shape):
        for cidx, cell in enumerate(row):
            region[ridx + dr][cidx + dc] = cell

    return region


def rotate_shape(shape):
    new_shape = copy.deepcopy(shape)
    width, height = len(shape[0]), len(shape)
    for ridx, row in enumerate(shape):
        for cidx, cell in enumerate(row):
            new_shape[height - 1 - cidx][ridx] = cell

    return new_shape


def generate_possible_places(region, shape):
    result = set()
    for ridx, row in enumerate(region):
        for cidx, _ in enumerate(row):
            if ridx + len(shape) <= len(region) and cidx + len(shape[0]) <= len(row):
                original = shape

                region_and_shape = copy.deepcopy(region)
                put_shape(region_and_shape, shape, ridx, cidx)
                result.add(get_taken(region_and_shape))

                shape = rotate_shape(shape)
                region_and_shape = copy.deepcopy(region)
                put_shape(region_and_shape, shape, ridx, cidx)
                result.add(get_taken(region_and_shape))

                shape = rotate_shape(shape)
                region_and_shape = copy.deepcopy(region)
                put_shape(region_and_shape, shape, ridx, cidx)
                result.add(get_taken(region_and_shape))

                shape = original

    return result



def fit(destination, places):
    result = set()
    for place in places:
        if not destination.intersection(place):
            result.add(frozenset(destination | place))

    return result


def get_taken(destination):
    taken_destination = set()
    for ridx, row in enumerate(destination):
        for cidx, cell in enumerate(row):
            if cell == 1:
                taken_destination.add((ridx, cidx))

    return frozenset(taken_destination)


def put_n_shapes(destinations, places, n):
    if n == 0:
        return destinations

    new_destinations = set()
    for destination in destinations :
        new_destinations |= put_n_shapes(fit(destination, places), places, n - 1)

    print(n, len(new_destinations))
    return new_destinations

# 12x5: 1 0 1 0 2 2
width, height = 12, 5
quantity = [1, 0, 1, 0, 2, 2]

# 41x38: 26 26 29 23 21 30
width, height = 41, 38
quantity = [26, 26, 29, 23, 21, 30]

region = create_region(width, height)
destinations = [region]
possiblities = []
for shape_idx, q in enumerate(quantity):
    if q > 0:
        shape = shapes[shape_idx]
        places = generate_possible_places(region, shape)
        n_shapes = put_n_shapes([set()], places, q)
        possiblities.append(n_shapes)
        print("XXX", len(n_shapes))

# print(possiblities)
