import math

with open("./resources/day1.txt") as f:
    data = f.read()

rotations = []
for line in data.strip().split("\n"):
    if line.startswith("L"):
        rotations.append(-int(line.replace("L", "")))
    else:
        rotations.append(int(line.replace("R", "")))


def part1():
    dial = 50
    zero_count = 0
    for rotation in rotations:
        dial += rotation
        if dial < 0 or dial > 99:
            dial %= 100

        if dial == 0:
            zero_count += 1

    print(zero_count)


def rotate(dial, rotation):
    zero_count = 0

    if rotation > 0:
        dial += rotation
        zero_count = int(dial / 100)
        dial %= 100

    elif rotation < 0:
        if dial > 0 and (dial + rotation) % 100 > (dial + rotation) and abs(rotation) < 100:
            zero_count += 1
        elif dial + rotation < 0:
            zero_count += math.ceil((-rotation - dial) / 100)
            if dial == 0:
                zero_count -= 1

        dial = (dial + rotation) % 100
        if dial == 0:
            zero_count += 1

    return dial, zero_count


def part2():
    dial = 50
    zero_count = 0
    for rotation in rotations:
        dial, zero = rotate(dial, rotation)
        zero_count += zero

    print(zero_count)


part1()
part2()
