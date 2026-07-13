def run(_):
    input = 312051
    grid = {}
    x = y = 0
    grid[(x, y)] = 1
    dir_idx = 0
    dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    adj = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    while True:
        dx, dy = dirs[dir_idx]
        x += dx
        y += dy
        num = sum(grid.get((x + ax, y + ay), 0) for ax, ay in adj)
        if num > input:
            print(num)
            break

        grid[(x, y)] = num
        next_idx = (dir_idx + 1) % 4
        nx, ny = dirs[next_idx]
        if (x + nx, y + ny) not in grid:
            dir_idx = next_idx
