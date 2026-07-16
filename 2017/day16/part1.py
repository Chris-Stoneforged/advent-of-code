def run(source):
    moves = open(source).readline().rstrip().split(",")
    programs = [chr(i) for i in range(97, 113)]

    for move in moves:
        if move[0] == "s":
            idx = len(programs) - int(move[1:])
            programs = [*programs[idx:], *programs[:idx]]
        elif move[0] == "p":
            a, b = [programs.index(x) for x in move[1:].split("/")]
            programs[a], programs[b] = programs[b], programs[a]
        elif move[0] == "x":
            a, b = [int(x) for x in move[1:].split("/")]
            programs[a], programs[b] = programs[b], programs[a]

    print("".join(programs))
