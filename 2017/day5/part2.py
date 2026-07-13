def run(source):
    jumps = [int(l.rstrip()) for l in open(source).readlines()]
    index = 0
    steps = 0

    try:
        while True:
            jump = jumps[index]
            increment = -1 if jump >= 3 else 1
            jumps[index] = jumps[index] + increment
            index += jump
            steps += 1
    except IndexError:
        print(steps)
