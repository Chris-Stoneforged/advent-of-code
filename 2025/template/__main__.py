import sys
import time

def main():
    start_time = time.time()

    is_test = len(sys.argv) > 1 and sys.argv[1] == "test"
    file_name = "test" if is_test else "source"
    file = open(f"{sys.argv[0]}/{file_name}.txt")

    for line in file:
        print(line.rstrip())

    # Work goes here

    time_taken = time.time() - start_time
    print(f"Time: {time_taken}")

if __name__ == "__main__":
    main()
