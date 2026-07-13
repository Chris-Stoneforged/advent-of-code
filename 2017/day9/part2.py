def run(source):
    stream = open(source).readline().rstrip()
    garbage = 0
    states = ["group"]

    for char in stream[1:]:
        if states[-1] == "group":
            if char == "{":
                states.append("group")
            elif char == "}":
                states.pop()
            elif char == "<":
                states.append("garbage")
            elif char == "!":
                states.append("escaped")
        elif states[-1] == "garbage":
            if char == ">":
                states.pop()
            elif char == "!":
                states.append("escaped")
            else:
                garbage += 1
        elif states[-1] == "escaped":
            states.pop()

    print(garbage)
