from functools import reduce


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
    x, y = reduce(lambda sum, cur: (sum[0] + cur[0], sum[1] + cur[1]), dirs)

    x = abs(x)
    y = abs(y)
    print((abs(x - y) // 2) + min(x, y) if y >= x else abs(x - y) + min(x, y))
