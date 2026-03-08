data = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

with open("./resources/day6.txt") as f:
    data = f.read()

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


final_arguments = []
for i, operation in enumerate(operations):
    if operation == "+":
        fn = add_list
    else:
        fn = mul_list

    values = [arg[i] for arg in arguments]
    result = fn(values)
    final_arguments.append(result)

final_result = sum(final_arguments)

print(final_result)
