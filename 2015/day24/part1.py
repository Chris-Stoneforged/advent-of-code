from itertools import combinations
from functools import reduce
from operator import mul

def run(source):
    weights = sorted(list(map(int, [l.rstrip() for l in open(source).readlines()])))
    gw = sum(weights) // 3
    for i in range(1, len(weights)):
        qes = []
        for c in combinations(weights, i):
            if sum(c) == gw:
                qes.append(reduce(mul, c, 1))
        if len(qes) > 0:
            print(min(qes))
            break

