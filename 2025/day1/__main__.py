with open("day1/source.txt") as file:
    lines = [line.rstrip() for line in file]

total_1 = 0
total_2 = 0
dial = 50

for line in lines:
    direction = line[0]
    amount = int(line[1:])

    if direction == "L":
        if dial == 0:
            total_2 -= 1

        dial -= amount
        while dial < 0:
            dial += 100

            total_2 += 1
        if dial == 0:
            total_1 += 1
            total_2 += 1

    if direction == "R":
        dial += amount
        while dial > 99:
            dial -= 100
            total_2 += 1

        if dial == 0:
            total_1 += 1

print(f"Part 1 total: {total_1}")
print(f"Part 2 total: {total_2}")
