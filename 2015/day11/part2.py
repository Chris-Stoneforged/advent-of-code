import re

def satisfies(input):
    has_incrementing = False
    for i in range(2, len(input)):
        if input[i] - input[i - 1] == -1 and input[i] - input[i - 2] == -2:
            has_incrementing = True
            break

    return re.search("([a-z])\\1.*([a-z])\\2", to_str(input)) and has_incrementing

def increment(input):
    for i in range(len(input)):
        input[i] += 1
        if input[i] in [105, 108, 111]:
            input[i] += 1
        if input[i] > 122:
            input[i] = 97
            continue
        break

def to_arr(s):
    return [ord(c) for c in reversed(s)]

def to_str(a):
    return "".join([chr(i) for i in reversed(a)])

def run(_):
    input = to_arr("cqjxxyzz")
    increment(input)
    while not satisfies(input):
        increment(input)

    print(to_str(input))
