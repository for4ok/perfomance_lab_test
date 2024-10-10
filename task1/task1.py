import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

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

print(result)
