from functools import reduce
from typing import List


def run(source):
    lengths = [ord(l) for l in open(source).readline().rstrip()]
    lengths.extend([17, 31, 73, 47, 23])
    sequence = [i for i in range(256)]
    skip_size = 0
    current = 0

    for _ in range(64):
        for l in lengths:
            for a, b in iter_reverse(current, l, len(sequence)):
                temp = sequence[a]
                sequence[a] = sequence[b]
                sequence[b] = temp
            current = (current + l + skip_size) % len(sequence)
            skip_size += 1

    print(
        "".join(
            [
                hex(reduce(lambda a, b: a ^ b, block))[2:4].zfill(2)
                for block in iter_block(sequence, 16)
            ]
        )
    )


def iter_reverse(current: int, length: int, size: int):
    start_idx = current
    end_idx = current + length - 1
    while start_idx < end_idx:
        yield (start_idx % size, end_idx % size)
        start_idx += 1
        end_idx -= 1


def iter_block(seq: List[int], block_size: int):
    for i in range(0, len(seq), block_size):
        yield seq[i : i + block_size]
