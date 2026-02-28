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
        while rotation > 0:
            d = min(100 - dial, rotation)
            dial += d
            if dial == 100:
                dial = 0
                zero_count += 1

            rotation -= d
    elif rotation < 0:
        while rotation < 0:
            if dial > 0:
                d = min(dial, -rotation)
            else:
                d = min(100, -rotation)
            dial -= d
            dial %= 100
            if dial == 0:
                zero_count += 1

            rotation += d

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
