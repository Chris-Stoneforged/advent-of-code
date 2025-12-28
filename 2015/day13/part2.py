import re
from itertools import permutations

def calculate_happiness(guests, scores):
    return sum([sum([scores[(a, b)] for a, b in zip(guests, guests[i:] + guests[:i])]) for i in [-1, 1]])

def run(source):
    scores = {}
    for line in open(source):
        a, sign, amount, b = re.match("^([A-Z][a-z]*).+(lose|gain) (\d+).+ ([A-z][a-z]*)\.$", line.strip()).groups()
        scores[(a, b)] = int(amount) if sign == "gain" else -int(amount)

    guests = set([a for a, _ in scores.keys()])

    guests.add("me")
    for g in guests:
        scores[(g, "me")] = 0
        scores[("me", g)] = 0

    print(max([calculate_happiness(p, scores) for p in permutations(guests)]))
