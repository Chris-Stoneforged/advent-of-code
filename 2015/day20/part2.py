import math

def find_factors(num):
    factors = set()
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    return [f for f in factors if f * 50 >= num]

def run(source):
    target = int(open(source).read().strip())
    house = 1
    while True:
        s = sum(i * 11 for i in find_factors(house))
        if s >= target:
            break
        house += 1
    print(house)
