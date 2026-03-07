data = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

with open("./resources/day3.txt") as f:
    data = f.read()

banks = []
for line in data.strip().split("\n"):
    bank = [int(c) for c in line]
    banks.append(bank)


def find_max(bank):
    largest = float("-inf")
    index = -1
    for i, battery in enumerate(bank):
        if battery > largest:
            largest = battery
            index = i

    return index, largest


def find_largest_joltage(bank, number_of_batteries):
    values = []
    index = 0
    for i in range(1, number_of_batteries + 1):
        if i == number_of_batteries:
            _, value = find_max(bank[index:])
        else:
            idx, value = find_max(bank[index:-number_of_batteries + i])
            index += idx + 1

        values.append(value)

    return int("".join(map(str, values)))


def part1():
    total = 0
    for bank in banks:
        total += find_largest_joltage(bank, 2)

    print(total)


def part2():
    total = 0
    for bank in banks:
        total += find_largest_joltage(bank, 12)

    print(total)


part1()
part2()
