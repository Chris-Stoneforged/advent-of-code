import sys
import time

def for_each_paper(grid, func):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == "@":
                func(i, j)  

def increment_surrounding(i, j, papers, increment):
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            k = (i + x, j + y)
            if k in papers:
                papers[k] += increment

def set_papers(i, j, papers, value):
    papers[(i, j)] = value

def main():
    start_time = time.time()

    file_name = "test" if len(sys.argv) > 1 and sys.argv[1] == "test" else "source"
    file = open(f"{sys.argv[0]}/{file_name}.txt")

    grid = []
    for line in file:
        grid.append(list(line.rstrip()))

    papers = dict()
    for_each_paper(grid, lambda i, j: set_papers(i, j, papers, 0))
    for_each_paper(grid, lambda i, j: increment_surrounding(i, j, papers, 1))
                    
    total = sum(1 for _, v in papers.items() if v < 4)
    print(f"Total: {total}")
    
    removed_rolls = 0
    while True:
        total = 0
        removable_indices = []
        for k, v in papers.items():
            if v < 4:
                total += 1
                removable_indices.append(k)

        if total == 0:
            break

        removed_rolls += total

        for index in removable_indices:
            i, j = index
            increment_surrounding(i, j, papers, -1) 
            del papers[index]

    print(f"Rolls removed: {removed_rolls}")

    time_taken = time.time() - start_time
    print(f"Time: {time_taken}")

if __name__ == "__main__":
    main()
