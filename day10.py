import heapq
from collections import defaultdict

import sympy as sp

data = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

with open("./resources/day10.txt") as f:
    data = f.read().strip()

machines = []
for line in data.strip().split("\n"):
    parts = line.split(" ")
    lights = parts[0]
    buttons = parts[1:-1]
    joltage = parts[-1]

    lights = lights.replace("[", "").replace("]", "")
    lights = tuple([True if l == "#" else False for l in lights])

    buttons = [eval(b) for b in buttons]
    buttons = tuple([b if type(b) is tuple else (b,) for b in buttons])

    joltage = joltage.replace("{", "").replace("}", "").split(",")
    joltage = tuple([int(j) for j in joltage])

    machines.append((lights, buttons, joltage))


def toggle_lights(current_state, button):
    state = list(current_state)
    for b in button:
        state[b] = not state[b]

    return tuple(state)


def find_lights(lights, buttons):
    min_sofar = float("inf")

    init_state = tuple([False] * len(lights))
    q = [(0, init_state, buttons)]
    seen  = defaultdict(lambda : float("inf"))
    heapq.heapify(q)

    while q:
        pressed, state, buttons = heapq.heappop(q)

        if pressed >= min_sofar:
            continue

        if pressed >= seen[state]:
            continue

        seen[state] = pressed

        if state == lights:
            min_sofar = min(min_sofar, pressed)
            return min_sofar

        for button in buttons:
            heapq.heappush(q,
                           (pressed + 1, toggle_lights(state, button), buttons[1:] + buttons[:1]))

    return min_sofar


def find_joltage(joltage, buttons):
    symbols = sp.symbols('a:z', integer=True)[0:len(buttons)]
    button_to_symbols = dict([(b, s) for b, s in zip(buttons, symbols)])
    eqs = []
    for i, _ in enumerate(joltage):
        cell = None
        possible_buttons = [button for button in buttons if i in button]
        for button in possible_buttons:
            if cell:
                cell += button_to_symbols[button]
            else:
                cell = button_to_symbols[button]

        cell -= joltage[i]
        eqs.append(cell)

    solution = sp.solve(eqs, symbols, dict=True)[0]

    free_syms = set()
    for s in [v.free_symbols for v in solution.values()]:
        free_syms |= s
    free_syms = list(free_syms)

    total_min = float("inf")
    if free_syms:
        if len(free_syms) == 1:
            for v0 in range(0, max(joltage)):
                current = {}
                for var, expr in solution.items():
                    current[var] = expr.subs(free_syms[0], v0)
                current[free_syms[0]] = v0

                if all([True if 0 <= v == int(v) else False for v in current.values()]):
                    total_min = min(total_min, sum(current.values()))

        elif len(free_syms) == 2:
            limit = min(50, max(joltage) // 2)
            for v0 in range(0, limit):
                for v1 in range(0, limit):
                    current = {}
                    for var, expr in solution.items():
                        current[var] = expr.subs(free_syms[0], v0).subs(free_syms[1], v1)
                        if current[var] < 0 or int(current[var]) != current[var]:
                            break
                    current[free_syms[0]] = v0
                    current[free_syms[1]] = v1

                    if all([True if 0 <= v == int(v) else False for v in current.values()]):
                        total_min = min(total_min, sum(current.values()))

        elif len(free_syms) == 3:
            limit = min(50, max(joltage) // 3)
            for v0 in range(0, limit):
                for v1 in range(0, limit):
                    for v2 in range(0, limit):
                        current = {}
                        for var, expr in solution.items():
                            current[var] = expr.subs(free_syms[0], v0).subs(free_syms[1], v1).subs(free_syms[2], v2)
                            if current[var] < 0 or int(current[var]) != current[var]:
                                break
                        current[free_syms[0]] = v0
                        current[free_syms[1]] = v1
                        current[free_syms[2]] = v2

                        if all([True if 0 <= v == int(v) else False for v in current.values()]):
                            total_min = min(total_min, sum(current.values()))
        else:
            raise f"ERROR {len(free_syms)} too many free symbols!"
    else:
        total_min = sum(solution.values())

    return total_min


def part1():
    total = 0
    for i, machine in enumerate(machines):
        lights, buttons, _ = machine
        total += find_lights(lights, buttons)

    print(f"part1={total}")


def part2():
    total = 0
    print(f"part2", end="")
    for i, machine in enumerate(machines):
        _, buttons, joltage = machine
        total += find_joltage(joltage, buttons)
        if i % 80 == 0:
            print()
        print(f".", end="")

    print(f"={total}")


part1()
part2()
