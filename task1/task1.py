import sys


def formula(n, m):
    task_array = list(range(1, n + 1))
    path = []
    index = 0

    while True:
        first_element = task_array[index]
        path.append(first_element)

        for _ in range(m - 1):
            index = (index + 1) % n

        if index == 0:
            break

    result = ''.join(map(str, path))
    return result


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <n> <m>")
        return

    n = int(sys.argv[1])
    m = int(sys.argv[2])
    result = formula(n, m)
    print(result)


if __name__ == "__main__":
    main()
