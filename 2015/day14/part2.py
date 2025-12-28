import re

class Reindeer:
    def __init__(self, speed, fly, rest):
        self.speed = speed
        self.fly = fly
        self.rest = rest
        self.distance = 0
        self.score = 0

def run(source):
    reindeer = []
    for line in open(source):
        name, speed, fly, rest = re.match("([A-Z][a-z]+).+ (\\d+).+ (\\d+).+ (\\d+)", line).groups()
        reindeer.append(Reindeer(int(speed), int(fly), int(rest)))

    for i in range(1, 2504):
        for r in reindeer:
            if 1 <= i % (r.fly + r.rest) <= r.fly:
                r.distance += r.speed
        furthest = max([r.distance for r in reindeer])
        for r in reindeer:
            r.score += 1 if r.distance == furthest else 0

    print(max([r.score for r in reindeer]))
