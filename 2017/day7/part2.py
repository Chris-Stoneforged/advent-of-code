import re
from typing import List


class Node:
    def __init__(self, name: str, weight: int, children: List[str]):
        self.name = name
        self.original_weight = weight
        self.weight = weight
        self.children = children

    def __repr__(self) -> str:
        return f"{self.name}, {self.weight}, {self.children}"


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
    if not root:
        return

    def check_weight(node_name: str) -> int:
        node = nodes.get(node_name)
        if node is None:
            return 0

        child_weights = []
        weight_counts = {}
        for child in node.children:
            child_weight = check_weight(child)
            child_weights.append(child_weight)
            weight_counts[child_weight] = weight_counts.get(child_weight, 0) + 1
        total_weight = node.weight + sum(child_weights)
        node.weight = total_weight

        if len(weight_counts) > 1:
            print(weight_counts)

        return total_weight

    check_weight(root)
