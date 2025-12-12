import sys
import time

def calculate_joltage(bank, num_batteries):
    bank_string = str(bank)
    bank_length = len(bank_string)

    return int(calculate_joltage_recursive(bank_string, 0, 0, num_batteries, bank_length))

def calculate_joltage_recursive(bank, index, recursions, num_batteries, len):
    highest = 0
    pos = 0
    end = len - num_batteries + recursions + 1

    for i in range(index, end):
        num = int(bank[i])
        if num > highest:
            highest = num
            pos = i

    if recursions + 1 >= num_batteries:
        return f"{highest}"

    next = calculate_joltage_recursive(bank, pos + 1, recursions + 1, num_batteries, len)
    return f"{highest}{next}"

def main():
    start_time = time.time()

    file_name = "test" if len(sys.argv) > 1 and sys.argv[1] == "test" else "source"
    file = open(f"{sys.argv[0]}/{file_name}.txt")

    banks = [line.rstrip() for line in file]

    total_joltage = 0
    for bank in banks:
        total_joltage += calculate_joltage(bank, 12)

    print(f"Total Joltage = {total_joltage}")

    time_taken = time.time() - start_time
    print(f"time: {time_taken}")

if __name__ == "__main__":
    main()
