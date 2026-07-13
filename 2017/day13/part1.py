def run(source):
    layers = {
        int(d): int(r)
        for d, r in [l.rstrip().split(": ") for l in open(source).readlines()]
    }

    max_depth = max(list(layers.keys()))
    severity = 0

    for current_time in range(max_depth + 1):
        depth = layers.get(current_time)
        if not depth:
            continue

        oscillation_time = (depth * 2) - 2
        if current_time % oscillation_time == 0:
            severity += depth * current_time

    print(severity)
