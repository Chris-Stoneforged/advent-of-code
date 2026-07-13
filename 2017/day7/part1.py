import re
from typing import List


class Node:
    def __init__(self, name: str, weight: int, children: List[str]):
        self.name = name
        self.weight = weight
        self.children = children


def run(source):
    lines = [l.rstrip() for l in open(source).readlines()]
    nodes = dict()
    unique_children = set()

    for l in lines:
        match = re.search("(\\w+) \\((\\d+)\\)(?: -> )?(.*)", l)
        if match:
            name, weight, children = match.groups()
            children = children.split(", ") if children != "" else []
            node = Node(name, int(weight), children)

            nodes[name] = node
            for child in children:
                unique_children.add(child)

    root = list(set(nodes.keys()) - unique_children)[0]
    print(root)
