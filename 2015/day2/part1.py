def run(source):
    total = 0
    for line in open(source):
        l, w, h = map(int, line.strip().split('x'))
        sides = [l * w, w * h, h * l]
        total += sum(sides) * 2 + min(sides)

    print(total)
