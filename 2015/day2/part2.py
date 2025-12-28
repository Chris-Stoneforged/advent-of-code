def run(source):
    total = 0
    for line in open(source):
        sides = sorted(list(map(int, line.strip().split('x'))))
        total += sides[0] * 2 + sides[1] * 2 + sides[0] * sides[1] * sides[2]

    print(total)
