import sys
import time
from collections import deque

def part1(t, b):
    indicator = 0
    queue = deque()
    for button in b:
        queue.append((button, indicator, 0))

    while True:
        but, ind, depth = queue.popleft()
        for i in but:
            ind ^= (1 << i)

        if ind == t:
            return depth + 1

        for button in b:
            if button != but:
                queue.append((button, ind, depth + 1))

def part2(b, j):
    joltage = [0] * len(j)
    queue = deque()
    for button in b:
        queue.append((button, joltage.copy(), 0))

    while True:
        but, jol, depth = queue.popleft()
        for i in but:
            jol[i] += 1

        if jol == j:
            return depth + 1

        for button in b:
            queue.append((button, jol.copy(), depth + 1))

def main():
    start_time = time.time()

    is_test = len(sys.argv) > 1 and sys.argv[1] == "test"
    file_name = "test" if is_test else "source"
    file = open(f"{sys.argv[0]}/{file_name}.txt")

    total = 0
    for line in file:
        target, *buttons, joltage = line.rstrip().split(' ')
        t = sum((1 if c == "#" else 0) << i for i, c in enumerate(list(target[1:-1])))
        b = [list(map(int, b[1:-1].split(","))) for b in buttons]
        j = list(map(int, joltage[1:-1].split(",")))
        total += part1(t, b)
 
    print(f"Total pushes = {total}")

    time_taken = time.time() - start_time
    print(f"Time: {time_taken}")

if __name__ == "__main__":
    main()
