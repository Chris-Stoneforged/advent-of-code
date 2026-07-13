def run(source):
    relations = [tuple(r.rstrip().split(" <-> ")) for r in open(source).readlines()]
    comms_map = {id: children.split(", ") for id, children in relations}
    seen = []
    stack = ["0"]

    while len(stack):
        for child in [c for c in comms_map[stack.pop()] if c not in seen]:
            seen.append(child)
            stack.append(child)

    print(len(seen))
