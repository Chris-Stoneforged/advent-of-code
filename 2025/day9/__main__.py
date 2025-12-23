import sys
import time

class Tile:
    def __init__(self, point_a, point_b):
        self.corner_a = point_a
        self.corner_b = point_b
        self.calculate_area()

    def calculate_area(self):
        x_distance = self.corner_a[0] + 1 - self.corner_b[0]
        y_distance = self.corner_a[1] + 1 - self.corner_b[1]
        self.area = abs(x_distance) * abs(y_distance)

def test_direction(points, origin, direction):
    valid_points = []

    if direction == 0:
        valid_points = [p for p in points if p[0] < origin[0] and p[1] == origin[1]]
        valid_points.sort(key=lambda p: p[0], reverse=True)
    elif direction == 2:
        valid_points = [p for p in points if p[0] > origin[0] and p[1] == origin[1]]
        valid_points.sort(key=lambda p: p[0])
    elif direction == 1:
        valid_points = [p for p in points if p[0] == origin[0] and p[1] < origin[1]]
        valid_points.sort(key=lambda p: p[1], reverse=True)
    elif direction == 3:
        valid_points = [p for p in points if p[0] == origin[0] and p[1] > origin[1]]
        valid_points.sort(key=lambda p: p[1])

    if len(valid_points) == 0:
        return None

    return valid_points[0]

def direction_to_string(direction):
    if direction == 0: return "left"
    if direction == 1: return "up"
    if direction == 2: return "right"
    if direction == 3: return "down"
    return ""

def main():
    start_time = time.time()

    is_test = len(sys.argv) > 1 and sys.argv[1] == "test"
    file_name = "test" if is_test else "source"
    file = open(f"{sys.argv[0]}/{file_name}.txt")

    points = []
    for line in file:
        points.append([int(x) for x in line.rstrip().split(',')])

    origin = points[0]
    vertices = []
    current = None
    iterations = 0
    direction = 0

    print(origin)
    while current != origin and iterations < len(points):
        target = None
        while target == None:
            print(f"Testing {direction_to_string(direction % 4)}")
            t = test_direction(points, current or origin, direction % 4)
            if not t in vertices:
                target = t

            direction = direction + 1

        current = target
        vertices.append(current)
        iterations += 1

        print(f"Selected {target}")

    tiles = []

    for i in range(0, len(points)):
        for j in range(i + 1, len(points)):
            point_a = points[i]
            point_b = points[j]
            tiles.append(Tile(point_a, point_b))

    tiles_sorted = sorted(tiles, key = lambda p: p.area)
    print(f"Largest area = {tiles_sorted[-1].area}")

    time_taken = time.time() - start_time
    print(f"Time: {time_taken}")

if __name__ == "__main__":
    main()
