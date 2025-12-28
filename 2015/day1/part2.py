def run(source):
    total = 0
    for i, f in enumerate(list(map(lambda x: 1 if x == '(' else -1, open(source).readline().strip()))):
        total += f
        if total < 0:
            print(i + 1)
            break
