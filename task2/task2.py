import sys
import math


def read_circle_data(filename):
    with open(filename, 'r') as file:
        circle_center = tuple(map(int, file.readline().strip().split()))
        radius = int(file.readline().strip())
    return circle_center, radius


def read_points(filename):
    with open(filename, 'r') as file:
        points = [tuple(map(int, line.strip().split())) for line in file]
    return points


def point_position(point, circle_center, radius):
    distance = math.sqrt((point[0] - circle_center[0]) ** 2 + (point[1] - circle_center[1]) ** 2)
    if distance < radius:
        return 1  # Точка внутри круга
    elif distance == radius:
        return 0  # Точка на круге
    else:
        return 2  # Точка вне круга


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <circle_file> <points_file>")
        return

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    circle_center, radius = read_circle_data(circle_file)
    points = read_points(points_file)

    results = [point_position(point, circle_center, radius) for point in points]

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
