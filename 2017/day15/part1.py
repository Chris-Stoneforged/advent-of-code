def run(_):
    judge_score = 0
    mask = pow(2, 16) - 1
    divisor = 2147483647
    a = generator(679, 16807, divisor)
    b = generator(771, 48271, divisor)

    for _ in range(40000000):
        if next(a) & mask == next(b) & mask:
            judge_score += 1

    print(judge_score)


def generator(value, factor, divisor):
    while True:
        value = (value * factor) % divisor
        yield value
