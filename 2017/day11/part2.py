def run(source):
    dir_to_coord = {
        "n": (0, 2),
        "s": (0, -2),
        "ne": (1, 1),
        "se": (1, -1),
        "nw": (-1, 1),
        "sw": (-1, -1),
    }

    dirs = [dir_to_coord[d] for d in open(source).readline().rstrip().split(",")]
    x = y = 0
    steps = []
    for dx, dy in dirs:
        x += dx
        y += dy
        steps.append(calculate_steps(x, y))

    print(max(steps))


def calculate_steps(x, y) -> int:
    x = abs(x)
    y = abs(y)
    return (abs(x - y) // 2) + min(x, y) if y >= x else abs(x - y) + min(x, y)
