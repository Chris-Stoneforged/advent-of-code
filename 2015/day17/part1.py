from itertools import accumulate, combinations

def run(source):
    containers = sorted([int(l.rstrip()) for l in open(source)])
    liquid = 150
    
    max_idx = 0
    for i, c in enumerate(accumulate(containers), start=1):
        if c > liquid:
            max_idx = i
            break
    min_idx = 0
    for i, c in enumerate(accumulate(containers[::-1]), start=1):
        if c > liquid:
            min_idx = i
            break

    combos = []
    for i in range(min_idx, max_idx + 1):
        for c in combinations(containers, i):
            if sum(c) == liquid:
                combos.append(c)

    print(len(combos))
