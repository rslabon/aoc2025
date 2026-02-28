with open("./resources/day1.txt") as f:
    data = f.read().strip()

rotations = []
for line in data.split("\n"):
    if line.startswith("L"):
        rotations.append(-int(line.replace("L", "")))
    else:
        rotations.append(int(line.replace("R", "")))


def part1():
    dial = 50
    zero_count = 0
    for rotation in rotations:
        dial += rotation
        if dial < 0 or dial > 90:
            dial %= 100

        if dial == 0:
            zero_count += 1

    print(zero_count)


part1()
