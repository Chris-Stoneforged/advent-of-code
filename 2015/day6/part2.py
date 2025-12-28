import re

def turn_on(lights, new, max_volume):
    new_lights = {}
    remaining = new.copy()

    if max_volume == 0:
        new_lights[1] = new
    else:
        for i in range(max_volume, 0, -1):
            new_lights[i + 1] = (lights.get(i + 1, set()) - new) | (lights.get(i, set()) & new)
            remaining -= lights.get(i, set())
        new_lights[1] = (lights.get(1, set()) - new) | remaining

    return new_lights

def turn_off(lights, new, max_volume):
    new_lights = {}

    if max_volume > 0:
        for i in range(2, max_volume + 1):
            new_lights[i - 1] = (lights.get(i - 1, set()) - new) | (lights.get(i, set()) & new)
        new_lights[max_volume] = lights.get(max_volume, set()) - new

    return new_lights

def toggle(lights, new, max_volume):
    new_lights = {}
    remaining = new.copy()

    if max_volume == 0:
        new_lights[2] = new
    else:
        for i in range(max_volume, 0, -1):
            new_lights[i + 2] = (lights.get(i + 2, set()) - new) | (lights.get(i, set()) & new)
            remaining -= lights.get(i, set())
        new_lights[2] = (lights.get(2, set()) - new) | remaining
        new_lights[1] = lights.get(1, set()) - new

    return new_lights

def run(source):
    lights = {}
    max_volume = 0

    for line in open(source):
        match = re.match("(turn on|turn off|toggle)\\s(\\d+,\\d+)\\sthrough\\s(\\d+,\\d+)", line)
        if match is None: continue

        action, a, b = match.groups()
        a = tuple(map(int, a.split(',')))
        b = tuple(map(int, b.split(',')))
        new = set([(x, y) for x in range(a[0], b[0] + 1) for y in range(a[1], b[1] + 1)])

        moves = {"turn on": turn_on, "turn off": turn_off, "toggle": toggle}
        lights = moves[action](lights, new, max_volume)
        max_volume = max([k for k in lights.keys()]) if len(lights) > 0 else 0

    print(sum([k * len(v) for k, v in lights.items()]))
