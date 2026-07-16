import re
import math


def run(source):
    lowest_a = math.inf
    lowest_p = 0

    for i, line in enumerate(open(source).readlines()):
        result = re.findall("<(-?\\d+),(-?\\d+),(-?\\d+)>", line)
        if not result:
            continue

        a = sum(abs(int(x)) for x in result[2])
        if a < lowest_a:
            lowest_a = a
            lowest_p = i

    print(lowest_p)
