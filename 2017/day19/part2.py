def run(source):
    map = [list(l.rstrip()) for l in open(source).readlines()]
    x, y = (map[0].index("|"), 0)
    dir = (0, 1)
    steps = 1

    is_within_grid = lambda x, y: y >= 0 and y < len(map) and x >= 0 and x < len(map[y])

    while True:
        dx, dy = dir
        x += dx
        y += dy
        current = map[y][x]

        if current == " ":
            break
        if current == "+":
            if dir[0] != 0:  # Moving horizontal
                if is_within_grid(x, y + 1) and map[y + 1][x] != " ":
                    dir = (0, 1)
                elif is_within_grid(x, y - 1) and map[y - 1][x] != " ":
                    dir = (0, -1)
            elif dir[1] != 0:  # Moving vertical
                if is_within_grid(x + 1, y) and map[y][x + 1] != " ":
                    dir = (1, 0)
                elif is_within_grid(x - 1, y) and map[y][x - 1] != " ":
                    dir = (-1, 0)

        steps += 1

    print(steps)
