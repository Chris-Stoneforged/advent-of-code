from functools import reduce


def run(source):
    groups = []
    for line in open(source).readlines():
        id, children = line.rstrip().split(" <-> ")
        group = set([id, *(children.split(", "))])
        intersecting = [g for g in groups if len(g & group) > 0]
        merged = reduce(lambda sum, cur: sum | cur, [group, *intersecting])
        groups = [merged, *[g for g in groups if g not in intersecting]]

    print(len(groups))
