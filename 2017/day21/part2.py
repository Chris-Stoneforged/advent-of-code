import math


def run(source):
    instructions = []
    for line in open(source).readlines():
        f, t = line.rstrip().split(" => ")
        instructions.append([*get_variants(string_to_grid(f)), string_to_grid(t)])

    # first grid cannot be divided so convert is as the first step
    grid = convert_grid([[0, 1, 0], [0, 0, 1], [1, 1, 1]], instructions)
    iterations = 18

    for _ in range(iterations - 1):
        grids = split_grid(grid)
        converted = [convert_grid(g, instructions) for g in grids]
        grid = stitch_grids(converted)

    print(sum(sum(x) for x in grid))


def string_to_grid(string):
    return [[1 if i == "#" else 0 for i in x] for x in string.split("/")]


def split_grid(grid):
    split_grids = []
    step = 2 if len(grid) % 2 == 0 else 3

    for y in range(0, len(grid), step):
        for x in range(0, len(grid), step):
            split_grids.append(
                [[grid[y + i][x + j] for j in range(step)] for i in range(step)]
            )

    return split_grids


def stitch_grids(grids):
    grid = []
    step = len(grids[0])
    width = int(math.sqrt(len(grids)))
    size = step * width

    for y in range(size):
        line = []
        for x in range(size):
            grid_index = ((y // step) * width) + (x // step)
            line.append(grids[grid_index][y % step][x % step])
        grid.append(line)

    return grid


def convert_grid(grid, instructions):
    for i in instructions:
        for r in i[:-1]:
            if grid == r:
                return i[-1]


def get_variants(grid):
    grids = []
    g = grid
    for _ in range(4):
        grids.append(g)
        g = rotate_grid_90_degrees_clockwise(g)
    g = flip_grid(g)
    for _ in range(4):
        grids.append(g)
        g = rotate_grid_90_degrees_clockwise(g)
    return grids


def rotate_grid_90_degrees_clockwise(grid):
    new = [[*x] for x in grid]  # Create copy to avoid mutating the original
    n = len(new)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = new[i][j]
            new[i][j] = new[n - 1 - j][i]
            new[n - 1 - j][i] = new[n - 1 - i][n - 1 - j]
            new[n - 1 - i][n - 1 - j] = new[j][n - 1 - i]
            new[j][n - 1 - i] = temp
    return new


def flip_grid(grid):
    return [list(reversed(row)) for row in grid]
