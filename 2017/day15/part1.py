def run(_):
    judge_score = 0
    a = 65
    b = 8921
    a_factor = 16807
    b_factor = 48271
    divisor = 2147483647
    mask = pow(2, 17) - 1

    for _ in range(40000000):
        a = (a * a_factor) % divisor
        b = (b * b_factor) % divisor
        # print(a, b)
        # print(bin(a))
        # print(bin(b))
        # print(bin(a & mask))
        # print(bin(b & mask))
        if a & mask == b & mask:
            judge_score += 1

        # print(judge_score)
        # input()

    print(judge_score)
