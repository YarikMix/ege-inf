for n in range(174457, 174505+1):
    arr = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            arr.extend([d, n // d])
        d += 1
    if len(arr) == 2:
        print(*arr)


"""
Ответ:
3 58153
7 24923
59 2957
13 13421
149 1171
5 34897
211 827
2 87251
"""