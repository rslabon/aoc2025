data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

with open("./resources/day2.txt", "r") as f:
    data = f.read().strip()

ranges = []
for part in data.split(","):
    start, end = part.split("-")
    start = int(start)
    end = int(end)
    ranges.append((start, end))


def find_invalid(start, end):
    result = set()
    for n in range(start, end + 1):
        s = str(n)
        if len(s) % 2 == 0:
            mid = len(s) // 2
            if s[0:mid] == s[mid:]:
                result.add(n)

    return result


def partition_by_size(list, size):
    result = []
    for i in range(0, len(list), size):
        result.append(list[i:i + size])

    return result


def find_invalid2(start, end):
    result = set()
    for n in range(start, end + 1):
        s = str(n)
        for size in range(1, 1 + len(s) // 2):
            sublists = partition_by_size(s, size)
            if len(set(sublists)) == 1:
                result.add(n)

    return result


def part1():
    invalid = []
    for start, end in ranges:
        invalid += find_invalid(start, end)

    print(sum(invalid))


def part2():
    invalid = []
    for start, end in ranges:
        invalid += find_invalid2(start, end)

    print(sum(invalid))


part1()
part2()
