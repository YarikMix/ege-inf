# Решение №1
from itertools import combinations


with open("inputA.txt") as f:
    arr = [int(i) for i in f.readlines()][1:]
    print(len([(a, b) for a, b in combinations(arr, 2) if (a * b) % 26 == 0]))


# Решение №2
from itertools import combinations


with open("inputA.txt") as f:
    count = 0
    for a, b in combinations(arr, 2):
        if (a * b) % 26 == 0:
        	count += 1
    print(count)

    
# Ответ: 19