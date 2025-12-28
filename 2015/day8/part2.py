def run(source):
    print(sum([len(l.strip().replace('\\', "\\\\").replace('\"', "\\\"")) + 2 - len(l.strip()) for l in open(source)]))
