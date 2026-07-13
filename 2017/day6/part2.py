from typing import List


def run(source):
    seen = []
    banks = [int(n) for n in open(source).readline().split("\t")]
    seen.append(banks)
    loops = 0

    while True:
        loops += 1
        index = banks.index(max(banks))
        banks = redistribute(banks, index)
        if banks in seen:
            break
        seen.append(banks)

    print(loops, banks)


def redistribute(banks, index) -> List[int]:
    new_banks = [b for b in banks]
    amount = new_banks[index]
    new_banks[index] = 0
    for _ in range(amount):
        index = (index + 1) % len(new_banks)
        new_banks[index] += 1
    return new_banks
