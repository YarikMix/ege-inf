# Решение №1
from itertools import combinations


with open("inputA.txt") as f:
    arr = [int(i) for i in f.readlines()][1:]

    res = [x[0] * x[1] for x in combinations(arr, 2) if x[0] * x[1] % 14 == 0]
    print(max(res))


# Решение №2
from itertools import combinations


with open("inputA.txt") as f:
    N = int(f.readline())
    max_R = 0
    arr = [int(f.readline()) for _ in range(N)]

    # Перебираем всевозможные пары чисел
    for a, b in combinations(arr, 2):
        if a * b % 14 == 0:
            max_R = max(max_R, a * b)
    print(max_R)


# Решение №3
with open("inputA.txt") as f:
    N = int(f.readline())
    max_R = 0
    arr = []
    for _ in range(N):
        arr.append(int(f.readline()))

    for i in range(0, N - 1):
        for j in range(i + 1, N):
            X = arr[i] * arr[j]
            if X % 14 == 0 and X > max_R:
                max_R = X

    print(max_R)


# Ответ: 719740