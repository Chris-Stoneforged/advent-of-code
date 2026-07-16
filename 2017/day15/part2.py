def run(_):
    judge_score = 0
    mask = pow(2, 16) - 1
    divisor = 2147483647
    a = generator(679, 16807, divisor, 4)
    b = generator(771, 48271, divisor, 8)

    for _ in range(5000000):
        a_value = next(a)
        b_value = next(b)
        if a_value & mask == b_value & mask:
            judge_score += 1

    print(judge_score)


def generator(value, factor, divisor, mod):
    while True:
        value = (value * factor) % divisor
        if value % mod == 0:
            yield value
