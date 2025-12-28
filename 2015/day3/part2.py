def run(source):
    moves = { '^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0) }
    x1 = x2 = y1 = y2 = 0
    locations = {(0, 0)}
    for i, (dx, dy) in enumerate(map(lambda x: moves[x], open(source).readline().strip())):
        if i % 2 == 0:
            x1, y1 = x1 + dx, y1 + dy
            locations.add((x1, y1))
        else:
            x2, y2 = x2 + dx, y2 + dy
            locations.add((x2, y2))

    print(len(locations))
