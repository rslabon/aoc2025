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
    result = []
    for n in range(start, end + 1):
        s = str(n)
        if len(s) % 2 == 0:
            mid = len(s) // 2
            if s[0:mid] == s[mid:]:
                result.append(n)

    return result


def part1():
    invalid = []
    for start, end in ranges:
        invalid += find_invalid(start, end)

    print(sum(invalid))


part1()
