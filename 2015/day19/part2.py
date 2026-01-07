def run(source):
    r, medicine = open(source).read().split("\n\n")

    tokens = sorted([l.split(" => ")[0] for l in r.split("\n")], key=lambda a: -len(a))
    medicine = medicine.strip().replace("Y", ",").replace("CRn", "(").replace("Rn", "(").replace("Ar", ")")
    for t in tokens:
        medicine = medicine.replace(t, 'X')

    steps = 0
    while True:
        if medicine == "X":
            break
        for i in ["XX", "X(X)", "X(X,X)", "X(X,X,X)", "(X)", "(X,X)", "(X,X,X)"]:
            idx = medicine.find(i)
            if idx >= 0:
                medicine = medicine[:idx] + 'X' + medicine[idx + len(i):]
                steps += 1
                break

    print(steps)
