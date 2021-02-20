# Решение только для A
from itertools import combinations


with open("inputA.txt") as f:
    arr = [int(i) for i in f.readlines()][1:]

    res = [x[0] * x[1] for x in combinations(arr, 2) if x[0] * x[1] % 14 == 0]
    print(max(res))

# A 719740