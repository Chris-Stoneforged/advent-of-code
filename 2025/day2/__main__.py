import sys
import time

def is_number_invalid(number, base):
    i_str = str(number)
    strlen = len(i_str)

    if strlen % base != 0:
        return False

    step = int(strlen / base)
    origin = i_str[:step]

    for i in range(step, strlen, step):
        if i_str[i:i + step] != origin:
            return False

    return True
    
def is_number_invalid_part2(number):
    for i in range(2, 10):
        if is_number_invalid(number, i):
            return True

    return False

def main():
    t = time.time()

    src = "test" if len(sys.argv) > 1 and sys.argv[1] == "test" else "source"
    with open(f"day2/{src}.txt") as file:
        ids = file.readline().rstrip().split(",")

    total_1 = 0
    total_2 = 0

    for id in ids:
        parts = id.split("-")
        first_id = int(parts[0])
        last_id = int(parts[1])

        for i in range(first_id, last_id + 1):
            if is_number_invalid(i, 2):
                total_1 += i
            if is_number_invalid_part2(i):
                total_2 += i

    print(f"Part 1 total: {total_1}")
    print(f"Part 2 total: {total_2}")
    print(f"Time: {time.time() - t}")

if __name__ == "__main__":
    main()
