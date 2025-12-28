def run(source):
    print(sum(list(map(lambda x: 1 if x == '(' else -1, open(source).readline().strip()))))
