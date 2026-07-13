from itertools import combinations
from math import fmod


def run(source):
    print(sum(get_div(l) for l in open(source).readlines()))


def get_div(line) -> int:
    nums = [int(c) for c in line.split("\t")]
    for a, b in combinations(nums, 2):
        if fmod(a, b) == 0:
            return a // b
        if fmod(b, a) == 0:
            return b // a
    return 0
