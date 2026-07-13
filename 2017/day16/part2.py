import time

c = 16


def run(source):
    moves = open(source).readline().rstrip().split(",")
    # moves = ["s1", "x3/4", "pe/b"]
    itoc = {i: chr(i + 97) for i in range(c)}
    ctoi = {chr(i + 97): i for i in range(c)}
    start = 0
    print_programs(itoc, start)
    processes = []

    for move in moves:
        if move[0] == "s":
            idx = c - int(move[1:])
            processes.append((spin, idx))
        elif move[0] == "x":
            a, b = [int(x) for x in move[1:].split("/")]
            processes.append((exchange, a, b))
        elif move[0] == "p":
            a, b = [x for x in move[1:].split("/")]
            processes.append((partner, a, b))

    s = time.time()
    for p in processes:
        start = p[0](itoc, ctoi, start, *p[1:])

    e = time.time()
    print(f"Took {e - s:.7f}s")
    print_programs(itoc, start)


def print_programs(itoc, s):
    i = s % c
    l = [i for i in itoc.values()]
    print("".join([*l[i:], *l[:i]]))


def spin(itoc, ctoi, s, i):
    return s + i


def exchange(itoc, ctoi, s, a, b):
    ai = (a + s) % c
    bi = (b + s) % c
    ctoi[itoc[ai]], ctoi[itoc[bi]] = ctoi[itoc[bi]], ctoi[itoc[ai]]
    itoc[ai], itoc[bi] = itoc[bi], itoc[ai]
    return s


def partner(itoc, ctoi, s, a, b):
    itoc[ctoi[a]], itoc[ctoi[b]] = itoc[ctoi[b]], itoc[ctoi[a]]
    ctoi[a], ctoi[b] = ctoi[b], ctoi[a]
    return s
