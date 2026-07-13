from functools import reduce
from typing import List, Tuple


def run(_):
    puzzle_input = "oundnydw"
    grid = {}
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(128):
        hash = knot_hash(f"{puzzle_input}-{i}")
        binary = "".join(bin(int(hex, 16))[2:].zfill(4) for hex in hash)
        for j, char in enumerate(binary):
            grid[(j, i)] = int(char)

    groups = 0
    evaluated: List[Tuple[int, int]] = []
    for i in range(128):
        for j in range(128):
            to_eval = [(j, i)]
            is_group = False

            while len(to_eval):
                coord = to_eval.pop()
                if coord in evaluated:
                    continue

                evaluated.append(coord)
                if grid.get(coord) == 0:
                    continue

                is_group = True
                x, y = coord
                to_eval.extend(
                    [
                        (x + dx, y + dy)
                        for dx, dy in neighbors
                        if (x + dx, y + dy) in grid
                    ]
                )

            if is_group:
                groups += 1

    print(groups)


def knot_hash(input) -> str:
    lengths = [ord(c) for c in input]
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

    return "".join(
        [
            hex(reduce(lambda a, b: a ^ b, block))[2:].zfill(2)
            for block in iter_block(sequence, 16)
        ]
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
