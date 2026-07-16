import re
from itertools import combinations


def run(source):
    particles = []
    to_coords = lambda t: list(int(i) for i in t)

    for line in open(source).readlines():
        result = re.findall("<(-?\\d+),(-?\\d+),(-?\\d+)>", line)
        if not result:
            continue

        particles.append(
            {
                "p": to_coords(result[0]),
                "v": to_coords(result[1]),
                "a": to_coords(result[2]),
            }
        )

    def simulate():
        for p in particles:
            p["v"] = [a + b for a, b in zip(p["v"], p["a"])]
            p["p"] = [a + b for a, b in zip(p["p"], p["v"])]

    for _ in range(100):
        simulate()

        to_destroy = set()
        for a, b in combinations(range(len(particles)), 2):
            if particles[a]["p"] == particles[b]["p"]:
                to_destroy.add(a)
                to_destroy.add(b)

        idxs = reversed(sorted(list(to_destroy)))
        for i in idxs:
            particles.pop(i)

    print(len(particles))
