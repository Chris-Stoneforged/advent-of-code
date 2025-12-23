import sys
import time

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)

def count_timelines(current, path = []):
    path.append(f"({current.x}, {current.y})")
    if len(current.children) == 0:
        #print(path)
        return 1

    total = 0
    for c in current.children:
        total += count_timelines(c, path)
        path.pop()

    return total

def get_parents(nodes, grid, x, y):
    parents = []
    yy = y - 1
    while yy >= 0:
        if grid[yy][x] == '^':
            break

        ns = [n for n in nodes if n.x == x and n.y == yy]
        parents.extend(ns)

        yy -= 1

    return parents

def main():
    start_time = time.time()

    file_name = "test" if len(sys.argv) > 1 and sys.argv[1] == "test" else "source"
    file = open(f"{sys.argv[0]}/{file_name}.txt")

    grid = [list(line.rstrip()) for line in file][::2]  # Every second line is full of blanks, so we can ignore them
    depth = len(grid)
    width = len(grid[0])

    root = Node(grid[0].index('S'), 0)
    nodes = [root]

    for y in range(1, depth):
        for x in range(0, width):
            if grid[y][x] != '^':
                continue

            child1 = Node(x - 1, y)
            child2 = Node(x + 1, y)
            nodes.append(child1)
            nodes.append(child2)
            parents = get_parents(nodes, grid, x, y)

            for p in parents:
                if child1 is not None:
                    p.add_child(child1)

                if child2 is not None:
                    p.add_child(child2)

    timelines = count_timelines(root)
    print(f"Total Timelines = {timelines}")

    time_taken = time.time() - start_time
    print(f"Time: {time_taken}")

if __name__ == "__main__":
    main()
