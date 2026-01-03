import sys
import part1
import part2

argc = len(sys.argv)
part = 2 if argc > 1 and sys.argv[1] == "2" else 1
test = "test" if (argc == 3 and sys.argv[2] == "test") or (argc == 2 and sys.argv[1] == "test") else "source"
input_file = f"{sys.argv[0]}/{test}.txt"

if part == 1:
    part1.run(input_file)
else:
    part2.run(input_file)
