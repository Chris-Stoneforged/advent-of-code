def run(source):
    jumps = [int(l.rstrip()) for l in open(source).readlines()]
    index = 0
    steps = 0

    try:
        while True:
            jump = jumps[index]
            jumps[index] = jumps[index] + 1
            index += jump
            steps += 1
    except IndexError:
        print(steps)
