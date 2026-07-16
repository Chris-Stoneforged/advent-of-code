def run(_):
    step = 367
    cur = 0
    next_to_zero = 0

    for i in range(1, 50000000):
        cur = ((cur + step) % i) + 1
        if cur == 1:
            next_to_zero = i

    print(next_to_zero)
