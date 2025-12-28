import re

def run(source):
    records = []
    for line in open(source):
        name, speed, fly, rest = re.match("([A-Z][a-z]+).+ (\\d+).+ (\\d+).+ (\\d+)", line).groups()
        speed, fly, rest = map(int, [speed, fly, rest])
        cycles, remaining = divmod(2503, fly + rest)
        distance = (speed *fly * cycles) + (speed * min(remaining, fly))
        records.append(distance)
    print(max(records))
