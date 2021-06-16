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
    max_X = 0
    arr = [int(f.readline()) for _ in range(N)]

    # Перебираем всевозможные пары чисел
    for a, b in combinations(arr, 2):
        if a * b % 14 == 0:
            max_X = max(max_X, a * b)
    print(max_X)


# Решение №3
with open("inputA.txt") as f:
    N = int(f.readline())
    max_X = 0
    arr = []
    for _ in range(N):
        arr.append(int(f.readline()))

    for i in range(0, N - 1):
        for j in range(i + 1, N):
            X = arr[i] * arr[j]
            if X % 14 == 0 and X > max_X:
                max_X = X

    print(max_X)


# Ответ: 447552