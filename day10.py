import heapq
from functools import cache

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
    buttons = tuple([eval(b) for b in buttons])
    machines.append((lights, buttons, joltage))


@cache
def toggle(machine, button):
    state = list(machine)
    if type(button) is tuple:
        for b in button:
            state[b] = not state[b]
    else:
        state[button] = not state[button]

    return tuple(state)


def find(lights, buttons):
    min_sofar = float("inf")

    init_state = tuple([False] * len(lights))
    q = [(0, init_state, lights, buttons, set())]
    heapq.heapify(q)

    while q:
        pressed, machine, lights, buttons, seen = heapq.heappop(q)

        if pressed >= min_sofar:
            continue

        if machine == lights:
            min_sofar = min(min_sofar, pressed)
            return min_sofar

        if machine in seen:
            continue

        for button in buttons:
            heapq.heappush(q,
                           (pressed + 1, toggle(machine, button), lights, buttons[1:] + buttons[:1], seen | {machine}))

    return min_sofar


def part1():
    total = 0
    for machine in machines:
        lights, buttons, _ = machine
        total += find(lights, buttons)

    print(total)


part1()
