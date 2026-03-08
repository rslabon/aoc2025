data = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

with open("./resources/day6.txt") as f:
    data = f.read()


def add_list(list):
    r = 0
    for item in list:
        r += item
    return r


def mul_list(list):
    r = 1
    for item in list:
        r *= item
    return r


def part1():
    lines = data.strip().split("\n")
    arguments = []
    operations = []
    for i, line in enumerate(lines):
        parts = line.strip().split(" ")
        parts = [part for part in parts if len(part.strip()) > 0]
        if i == len(lines) - 1:
            operations = parts
        else:
            parts = [int(part) for part in parts]
            arguments.append(parts)

    total = 0
    for i, operation in enumerate(operations):
        if operation == "+":
            fn = add_list
        else:
            fn = mul_list

        values = [arg[i] for arg in arguments]
        total += fn(values)

    print(total)


def part2():
    lines = data.split("\n")
    lines = [line for line in lines if len(line) > 0]
    bottom_line = lines[-1]
    i = 0
    operations = []
    while i < len(bottom_line):
        if bottom_line[i] != " ":
            if operations:
                operations[-1][2] = i - 1

            operations.append([bottom_line[i], i, len(bottom_line) - 1])

        i += 1

    total = 0
    for op, start, end in operations:
        numbers = []
        for i in range(start, end + 1):
            n = ""
            for line in lines[0:-1]:
                n += line[i]

            n = n.strip()
            if len(n) > 0:
                numbers.append(int(n))

        if op == "+":
            total += add_list(numbers)
        else:
            total += mul_list(numbers)

    print(total)


part1()
part2()
