import sys
import time

class CircuitSection:
    def __init__(self, point_a, point_b, d_squared):
        self.point_a = point_a
        self.point_b = point_b
        self.distance_squared = d_squared

def distance_squared_3d(point1, point2):
    return sum((point1[i] - point2[i]) ** 2 for i in [0, 1, 2])

def get_containing_circuit_index(circuits, junction_box):
    for circuit in circuits:
        if junction_box in circuit:
            return circuits.index(circuit)

    return None

def main():
    start_time = time.time()

    is_test = len(sys.argv) > 1 and sys.argv[1] == "test"
    file_name = "test" if len(sys.argv) > 1 and sys.argv[1] == "test" else "source"
    file = open(f"{sys.argv[0]}/{file_name}.txt")

    junction_boxes = []
    for line in file:
        junction_boxes.append([int(x) for x in line.rstrip().split(',')])

    circuits = {}
    conections = []

    for i in range(0, len(junction_boxes)):
        for j in range(i + 1, len(junction_boxes)):
            point_a = junction_boxes[i]
            point_b = junction_boxes[j]
            distance_squared = distance_squared_3d(point_a, point_b)
            conections.append(CircuitSection(point_a, point_b, distance_squared))

    connections_sorted = sorted(conections, key = lambda p: p.distance_squared)
    circuits = [[j] for j in junction_boxes]

    i = 0
    while True:
        conn = connections_sorted[i]
        a_i = get_containing_circuit_index(circuits, conn.point_a)
        b_i = get_containing_circuit_index(circuits, conn.point_b)

        if a_i != b_i:
            circuits[a_i] = circuits[a_i] + circuits[b_i]
            del circuits[b_i]
        
        if len(circuits) == 1:
            result = conn.point_a[0] * conn.point_b[0]
            break
        
        i += 1
    
    #circuits_sorted = sorted(circuits, key = lambda c: len(c))
    #result = len(circuits_sorted[-1]) * len(circuits_sorted[-2]) * len(circuits_sorted[-3])

    print(f"Result = {result}")

    time_taken = time.time() - start_time
    print(f"Time: {time_taken}")

if __name__ == "__main__":
    main()
