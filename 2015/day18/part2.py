from itertools import product

def print_grid(grid):
    for row in grid:
        print("".join(map(lambda x: '#' if x else '.', row)))

def add_corners(grid):
    corners = [(0, 0), (0, len(grid) - 1), (len(grid[0]) - 1, 0), (len(grid[0]) - 1, len(grid) - 1)]
    for x, y in corners: grid[x][y] = True

def increment(grid):
    new_grid = [row[:] for row in grid]
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            valid = lambda x, y, a, b: 0 <= x + a < len(grid[0]) and 0 <= y + b < len(grid) and (a, b) != (0, 0) and grid[x + a][y + b]
            on = sum([1 for a, b in product([-1, 0, 1], repeat=2) if valid(x, y, a, b)])
            new_grid[x][y] = True if (not grid[x][y] and on == 3) or (grid[x][y] and on in [2, 3]) else False

    add_corners(new_grid)
    return new_grid

def run(source):
    grid = [list(map(lambda x: True if x == '#' else False, line.rstrip())) for line in open(source)]
    add_corners(grid)
    for _ in range(100): 
        grid = increment(grid)
    print(sum([sum([1 for x in row if x]) for row in grid]))
