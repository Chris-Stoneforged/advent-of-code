def run(source):
    instructions = list(map(lambda l: l.strip().replace(",", "").split(' '), open(source).readlines()))
    i = 0
    regs = { "a": 0, "b": 0 }
    while 0 <= i < len(instructions):
        curr = instructions[i]
        op = curr[0]
        jmp = 1
        if op == "hlf":
            regs[curr[1]] //= 2
        elif op == "tpl":
            regs[curr[1]] *= 3
        elif op == "inc":
            regs[curr[1]] += 1
        elif op == "jmp":
            jmp = int(curr[1])
        elif op == "jie":
            if regs[curr[1]] % 2 == 0:
                jmp = int(curr[2])
        elif op == "jio":
            if regs[curr[1]] == 1:
                jmp = int(curr[2])
        i += jmp
    print(regs["b"])
