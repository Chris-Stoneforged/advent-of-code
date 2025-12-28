import re

def run(source):
    lights = set()
    for line in open(source):
        action, a, b = re.match("(turn on|turn off|toggle)\\s(\\d+,\\d+)\\sthrough\\s(\\d+,\\d+)", line).groups()
        a = tuple(map(int, a.split(',')))
        b = tuple(map(int, b.split(',')))
        new = set([(x, y) for x in range(a[0], b[0] + 1) for y in range(a[1], b[1] + 1)])

        if action == "toggle": lights ^= new
        elif action == "turn on": lights |= new
        elif action == "turn off": lights -= new

    print(len(lights))
