def run(source):
    input = 312051
    closest_square, steps = find_closest_square(input)
    num = closest_square * closest_square
    x = steps + 1
    y = steps + 1

    if num == input:
        print(x + y)
        return

    for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        for _ in range(closest_square + 1):
            num += 1
            x += dx
            y += dy
            if num == input:
                print(abs(x) + abs(y))
                return

    print(abs(x) + abs(y))


def find_closest_square(num):
    steps = 0
    for i in range(1, 10000, 2):
        if (i + 2) * (i + 2) > num:
            return (i, steps)
        steps += 1
    return (0, 0)
