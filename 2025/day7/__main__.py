import sys
import time

def count_timelines(grid, depth, max_depth, index, splitters):
    if depth == max_depth:
        return 1
 
    if (depth, index) in splitters:
        return sum([count_timelines(grid, depth + 1, max_depth, index + i, splitters) for i in [-1, 1]])
    else:
        return count_timelines(grid, depth + 1, max_depth, index, splitters)

def main():
    start_time = time.time()

    file_name = "test" if len(sys.argv) > 1 and sys.argv[1] == "test" else "source"
    file = open(f"{sys.argv[0]}/{file_name}.txt")

    grid = [list(line.rstrip()) for line in file][::2]  # Every second line is full of blanks, so we can ignore them
    max_depth = len(grid)
    root = grid[0].index('S')
    splits = set()
    splitters = set()

    for i in range(0, max_depth):
        for j in range(0, len(grid[0])):
            if grid[i][j] == '^':
                splitters.add((i, j))

    print(f"num splitters = {len(splitters)}")

    timelines = count_timelines(grid, 0, max_depth, root, splitters)
    total_splits = len(splits)

    print(f"Total Splits = {total_splits}")
    print(f"Total Timelines = {timelines}")

    time_taken = time.time() - start_time
    print(f"Time: {time_taken}")

if __name__ == "__main__":
    main()
