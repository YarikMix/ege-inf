def F(n):
    arr = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            arr.extend([d, n // d])
        d += 1
    return sorted(arr)

for n in range(210235, 210300+1):
    if len(F(n)) == 4:
        print(*F(n))


"""
Ответ:
2 4 52561 105122
2 4 52567 105134
2 4 52571 105142
"""