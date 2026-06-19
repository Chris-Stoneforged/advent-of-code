def run(source):
    input = [int(c) for c in open(source).readline().strip()]
    print(sum(c for c, m in halfway_cycle(input) if c == m))


def halfway_cycle(iterable):
    for i in range(len(iterable)):
        yield (iterable[i], iterable[(i + (len(iterable) // 2)) % len(iterable)])
