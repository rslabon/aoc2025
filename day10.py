import heapq
from collections import defaultdict
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
    q = [(0, init_state, buttons, set())]
    heapq.heapify(q)

    while q:
        pressed, state, buttons, seen = heapq.heappop(q)

        if pressed >= min_sofar:
            continue

        if state == lights:
            min_sofar = min(min_sofar, pressed)
            return min_sofar

        if state in seen:
            continue

        for button in buttons:
            heapq.heappush(q,
                           (pressed + 1, toggle_lights(state, button), buttons[1:] + buttons[:1], seen | {state}))

    return min_sofar


@cache
def toggle_joltage(current_state, button, n=1):
    state = list(current_state)
    for b in button:
        state[b] += n

    return tuple(state)


@cache
def distance_to_joltage(state, joltage):
    d = [float("inf")] * len(state)
    for i, _ in enumerate(state):
        if state[i] <= joltage[i]:
            d[i] = (joltage[i] - state[i]) ** 2

    return sum(d)


def find_joltage(joltage, buttons):
    min_sofar = float("inf")

    init_state = tuple([0] * len(joltage))
    q = [(0, 0, init_state, buttons)]
    heapq.heapify(q)
    cache = defaultdict(lambda: float("inf"))

    tick = 0
    while q:
        distance, pressed, state, buttons = heapq.heappop(q)

        if cache[state] <= pressed:
            continue

        cache[state] = pressed

        tick += 1

        if pressed >= min_sofar:
            continue

        if state == joltage:
            min_sofar = min(min_sofar, pressed)
            print(f"took {tick}", min_sofar)
            return min_sofar

        for button in buttons:
            new_state = toggle_joltage(state, button)
            new_distance = distance_to_joltage(new_state, joltage)
            if new_distance != float("inf"):
                heapq.heappush(q, (new_distance, pressed + 1, new_state, (buttons[1:] + buttons[:1])))

    return min_sofar


def part1():
    total = 0
    for machine in machines:
        lights, buttons, _ = machine
        total += find_lights(lights, buttons)

    print(total)


def part2():
    total = 0
    for i, machine in enumerate(machines):
        _, buttons, joltage = machine
        total += find_joltage(joltage, buttons)
        print(f"done {i + 1}/{len(machines)}")

    print(total)


# part1()
part2()
