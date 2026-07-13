def run(source):
    lengths = [int(l) for l in open(source).readline().rstrip().split(",")]
    sequence = [i for i in range(256)]
    skip_length = 0
    current = 0

    for l in lengths:
        for a, b in iter_reverse(current, l, len(sequence)):
            temp = sequence[a]
            sequence[a] = sequence[b]
            sequence[b] = temp
        current = (current + l + skip_length) % len(sequence)
        skip_length += 1

    print(sequence[0] * sequence[1])


def iter_reverse(current: int, length: int, size: int):
    start_idx = current
    end_idx = current + length - 1
    while start_idx < end_idx:
        yield (start_idx % size, end_idx % size)
        start_idx += 1
        end_idx -= 1
