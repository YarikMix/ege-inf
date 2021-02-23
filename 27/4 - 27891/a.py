# Решение №1
from itertools import combinations


with open("inputA.txt") as f:
    arr = [int(i) for i in f.readlines()][1:]

    res = [x[0] * x[1] for x in combinations(arr, 2) if x[0] * x[1] % 14 == 0]
    print(max(res))


# Решение №2
from itertools import combinations


with open("inputA.txt") as f:
    arr, max_x = [int(i) for i in f.readlines()][1:], 0

    for couple in combinations(arr, 2):
        """Проходимся циклом по всем сочетаниям из двух элементов."""
        X = couple[0] * couple[1]
        if X % 14 == 0:
            max_x = max(max_x, X)
    print(max_x)


# Решение №3
with open("inputA.txt") as f:
    n = int(f.readline())
    arr, result = [int(f.readline()) for i in range(n)], 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            r = arr[i] * arr[j]
            if r % 14 == 0 and r > result:
                result = r
    print(result)

# A 447552