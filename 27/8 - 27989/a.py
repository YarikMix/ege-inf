# Решение только для A
from itertools import combinations


with open("inputA.txt") as f:
    arr = [int(i) for i in f.readlines()][1:]

    res = list(filter(lambda x: x[0] * x[1] % 26 == 0, combinations(arr, 2)))
    print(len(res))

# Альтернативное решение
from itertools import combinations


with open("inputA.txt") as f:
    arr, max_x = [int(i) for i in f.readlines()][1:], 0

    res = [x[0] * x[1] for x in combinations(arr, 2) if x[0] * x[1] % 26 == 0]
    print(len(res))

# A 19