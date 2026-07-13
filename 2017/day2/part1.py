def run(source):
    print(sum(get_diff(l) for l in open(source).readlines()))


def get_diff(line) -> int:
    nums = sorted([int(c) for c in line.split("\t")])
    return nums[-1] - nums[0]
