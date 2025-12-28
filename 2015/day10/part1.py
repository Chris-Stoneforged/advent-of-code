def run(_):
    current = "1113222113"
    iterations = 40

    for _ in range(iterations):
        next = ""
        char = current[0]
        counter = 1

        for c in current[1:]:
            if c == char:
                counter += 1
                continue
            next += f"{counter}{char}"
            char = c
            counter = 1

        next += f"{counter}{char}"
        current = next

    print(len(current))
