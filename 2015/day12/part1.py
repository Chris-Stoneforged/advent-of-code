import json

def walk(json, ints):
    if isinstance(json, dict):
        for _, v in json.items():
            walk(v, ints)
    elif isinstance(json, list):
        for item in json:
            walk(item, ints)
    elif isinstance(json, int):
        ints.append(json)

def run(source):
    j = json.load(open(source))
    ints = []
    walk(j, ints)
    print(sum(ints))
