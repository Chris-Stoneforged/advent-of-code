def run(source):
    vals = {}
    ops = { 
        "AND": lambda a, b: a & b,
        "OR": lambda a, b: a | b,
        "LSHIFT": lambda a, b: a << b,
        "RSHIFT": lambda a, b: a >> b,
    }
    unsolved = {}

    def get_value(x):
        print(f"Getting value {x}")
        try:
            return int(x)
        except:
            if x in vals:
                return vals[x]
            solve(x)
            return vals[x]

    def solve(val):
        if not val in unsolved:
            return

        eq = unsolved[val]
        print(f"Attempting to solve {val} = {eq}")
        eq_parts = eq.strip().split(' ')
        num_parts = len(eq_parts)

        if num_parts == 1:  # Single value plugged into a wire
            vals[val] = get_value(eq_parts[0])
        elif num_parts == 2:  # Only op with just two values is NOT
            vals[val] = ~get_value(eq_parts[1]) & 65535
        else:   # Has 3 values
            vals[val] = ops[eq_parts[1]](get_value(eq_parts[0]), get_value(eq_parts[2]))

        print(f"Solved {val}")
        unsolved.pop(val)

    for line in open(source):
        eq, res = line.strip().split("->")
        unsolved[res.strip()] = eq.strip()

    while len(unsolved) > 0:
        solve(list(unsolved.keys())[0])

    print(vals["a"])
