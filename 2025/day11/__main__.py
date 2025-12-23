import sys
import time

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []
        self.visited = False
        self.solo_outs = 0
        self.outs_with_fft = 0
        self.outs_with_dac = 0
        self.valid_paths = 0

    def add_child(self, child):
        self.children.append(child)

def get_or_create_node(nodes, name):
    if name in nodes:
        node = nodes[name]
    else:
        node = Node(name)
        nodes[name] = node

    return node

def count_outs(current, path = []):
    if current.visited:
        return

    if current.name == "out":
        path.append("out")
        print(f"Found out at: {path}")
        current.solo_outs = 1
        path.pop()
        return

    for child in current.children:
        path.append(current.name)
        count_outs(child, path)
        path.pop()
        current.solo_outs += child.solo_outs
        current.outs_with_dac += child.outs_with_dac
        current.outs_with_fft += child.outs_with_fft
        current.valid_paths += child.valid_paths

    if current.name == "dac":
        current.outs_with_dac += current.solo_outs
        current.valid_paths += current.outs_with_fft
        current.solo_outs = 0
        current.outs_with_fft = 0
    elif current.name == "fft":
        current.outs_with_fft += current.solo_outs
        current.valid_paths += current.outs_with_dac
        current.solo_outs = 0
        current.outs_with_dac = 0

    print(f"N: {current.name}, S: {current.solo_outs}, F: {current.outs_with_fft}, D: {current.outs_with_dac}, V: {current.valid_paths}")

    current.visited = True

def main():
    start_time = time.time()

    is_test = len(sys.argv) > 1 and sys.argv[1] == "test"
    file_name = "test" if is_test else "source"
    file = open(f"{sys.argv[0]}/{file_name}.txt")

    nodes = {}
    root = None

    for line in file:
        name = line[:3]
        outputs = line[5:].rstrip().split(' ')

        node = get_or_create_node(nodes, name)

        for out in outputs:
            child = get_or_create_node(nodes, out, node)
            node.add_child(child)

        if name == "svr":
            root = node

    count_outs(root)
    print(f"Total valid routes to out = {root.valid_paths}")

    time_taken = time.time() - start_time
    print(f"Time: {time_taken}")

if __name__ == "__main__":
    main()
