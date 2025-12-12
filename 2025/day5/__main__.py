import sys
import time

def main():
    start_time = time.time()

    file_name = "test" if len(sys.argv) > 1 and sys.argv[1] == "test" else "source"
    file = open(f"{sys.argv[0]}/{file_name}.txt")

    items = [line.rstrip() for line in file]
    space_index = items.index("")
    mins = [int(i.split("-")[0]) for i in items[:space_index]]
    maxs = [int(i.split("-")[1]) for i in items[:space_index]]
    ids = [int(i) for i in items[space_index + 1:]]

    mins.sort()
    maxs.sort()

    total = 0
    current_min = mins[0]
    current_max = maxs[0]

    for i in range(1, len(mins)):
        min = mins[i]
        max = maxs[i]

        if min > current_max:
            total += current_max - current_min + 1
            current_min = min
        
        current_max = max

    total += current_max - current_min + 1
    print(f"Total fresh: {total}")            

    time_taken = time.time() - start_time
    print(f"Time: {time_taken}")

if __name__ == "__main__":
    main()
