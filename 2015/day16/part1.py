import re

def run(source):
    target = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}
    for line in open(source):
        matches = [m for m in re.findall("([a-z]+: \\d+)", line)]
        atts = {m.split(": ")[0]: int(m.split(": ")[1]) for m in matches}
        if all([k not in atts or atts[k] == v for k, v in target.items()]):
            print(int("".join(line[3:line.index(':')])))
            break
