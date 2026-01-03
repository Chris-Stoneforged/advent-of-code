import re
from functools import reduce
from itertools import combinations

def partitions(n, k):
    for c in combinations(range(n + k - 1), k - 1):
        yield [b - a - 1 for a, b in zip((-1,) + c, c + ( n + k - 1,))]

def run(source):
    p = ".* (-?\\d+).* (-?\\d+).* (-?\\d+).* (-?\\d+).* (-?\\d+).*"
    props = ["c", "d", "f", "t"]

    ingredients = [{a: int(b) for a, b in zip(props, re.match(p, l).groups())} for l in open(source).readlines()]

    def solve(items, counts):
        return reduce(lambda a, b: a * b, [max(0, sum([a[p] * b for a, b in zip(items, counts)])) for p in props], 1)

    print(max(solve(ingredients, i) for i in partitions(100, len(ingredients))))
