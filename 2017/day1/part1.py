def run(source):
    input = [int(c) for c in open(source).readline().strip()]
    print(sum(c for c, m in pairwise(input) if c == m))


def pairwise(iterable):
    for i in range(1, len(iterable)):
        yield (iterable[i - 1], iterable[i])
    yield (iterable[-1], iterable[0])
