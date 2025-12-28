def run(source):
    original = []
    execed = []
    locs = {"total": 0}
    for line in open(source):
        #exec(f"execed.append(len({line.rstrip()}))", globals(), {"execed": execed})
        exec(f"total += {len(line.rstrip())} - len({line.rstrip()})", globals(), locs)
        #original.append(len(line.rstrip()))
    #print(sum([a - b for a, b in zip(original, execed)]))
    print(locs["total"])
