data = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

with open("./resources/day3.txt") as f:
    data = f.read()


def find_max(bank):
    largest = float("-inf")
    index = -1
    for i, battery in enumerate(bank):
        if battery > largest:
            largest = battery
            index = i

    return index, largest


def find_largest_joltage(bank):
    first_index, first_value = find_max(bank[0:-1])
    _, second_value = find_max(bank[first_index + 1:])
    return int(f"{first_value}{second_value}")


def part1():
    banks = []
    for line in data.strip().split("\n"):
        bank = [int(c) for c in line]
        banks.append(bank)

    total = 0
    for bank in banks:
        total += find_largest_joltage(bank)

    print(total)


part1()
