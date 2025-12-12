import sys
import time

def solve_problem(numbers, length, symbol):
    total = 0 if symbol == "+" else 1

    for i in range(-1, -length - 1, -1):
        number_string = ""

        for n in numbers:
            try:
                number_string += n[i]
            except:
                continue

        if symbol == "+":
            total += int(number_string)
        else:
            total *= int(number_string)

    return total

def main():
    start_time = time.time()

    file_name = "test" if len(sys.argv) > 1 and sys.argv[1] == "test" else "source"
    file = open(f"{sys.argv[0]}/{file_name}.txt")

    # Importantly, we must keep the spaces at the end, so just remove newline
    lines = [line.removesuffix('\n') for line in file]
    last = lines[-1]
    columns = []
    prev = len(last)
    total = 0

    for i in range(prev - 1, -1, -1):
        if last[i] != ' ':
            columns.append((i, prev - i))
            prev = i - 1

    for i, l in columns:
        problem = [lines[j][i:i + l] for j in range(0, len(lines))]
        total += solve_problem(problem[:-1], l, problem[-1].strip())

    print(f"Total = {total}")

    time_taken = time.time() - start_time
    print(f"Time: {time_taken}")

if __name__ == "__main__":
    main()
