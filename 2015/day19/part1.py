def run(source):
    r, medicine = open(source).read().split("\n\n")
    replacements = {}
    results = set()

    for re in r.split("\n"):
        molecule, result = re.split(" => ")
        if molecule in replacements:
            replacements[molecule].append(result)
        else:
            replacements[molecule] = [result]

    for k, v in replacements.items():
        curr_idx = 0
        while True:
            idx = medicine.find(k, curr_idx)
            if idx == -1: break
            for r in v:
                s = medicine[:idx] + r + medicine[idx + len(k):]
                results.add(s)
            curr_idx = idx + 1

    print(len(results))
