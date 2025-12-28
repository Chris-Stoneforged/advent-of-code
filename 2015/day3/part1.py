def run(source):
    moves = { '^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0) }
    x = y = 0
    locations = {(0, 0)}
    for dx, dy in map(lambda x: moves[x], open(source).readline().strip()):
        x, y = x + dx, y + dy
        locations.add((x, y))

    print(len(locations))
