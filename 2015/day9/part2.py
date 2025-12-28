import re

def run(source):
    distances = {}
    cities = set()
    totals = []

    for line in open(source):
        a, b, dist = re.match("([A-Za-z]+) to ([A-Za-z]+) = (\\d+)", line).groups()
        cities.add(a)
        cities.add(b)
        distances[(a, b)] = int(dist)
        distances[(b, a)] = int(dist)

    def search(curr, prev = None, visited = [], total = 0):
        visited.append(curr)
        this_dist = 0 if prev is None else distances[(prev, curr)]
        next = [c for c in cities if not c in visited]
        if len(next) == 0:
            totals.append(([v for v in visited], total + this_dist))
        else:
            for c in next:
                search(c, curr, visited, total + this_dist)
        visited.pop()

    for c in cities:
        search(c)

    print(max([t[1] for t in totals]))
