from collections import deque

def run(source):
    r, medicine = open(source).read().split("\n\n")
    medicine = medicine.strip()
    replacements = {}
    results = set()

    for re in r.split("\n"):
        molecule, result = re.split(" => ")
        if molecule in replacements:
            replacements[molecule].append(result)
        else:
            replacements[molecule] = [result]

    q = deque()
    q.extend([("e", "e", r, 1) for r in replacements["e"]])

    while len(q) > 0:
        total, to_replace, replacement, moves = q.popleft()
        curr_idx = 0

        while True:
            idx = total.find(to_replace, curr_idx)
            if idx == -1: 
                break

            new_str = total[:idx] + replacement
            if idx + len(to_replace) < len(total):
                new_str += total[idx + len(to_replace):]

            if new_str == medicine: 
                print(new_str, moves)
                exit()

            for k, v in replacements.items():
                if k not in new_str: continue
                q.extend([(new_str, k, r, moves + 1) for r in v])

            curr_idx = idx + 1
