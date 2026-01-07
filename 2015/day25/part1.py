def run(_):
    r, c, t = (2978, 3083, 20151125)
    for _ in range(sum(range(c + r - 1)) + c - 1):
        t = (t * 252533) % 33554393
    print(t)
