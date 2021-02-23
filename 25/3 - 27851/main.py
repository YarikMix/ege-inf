def f(n):
    """Нахождение всех делителей числа,
    не считая единицы и самого числа."""
    arr = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            arr.extend([d, n // d])
        d += 1
    return sorted(arr)

    
for n in range(210235, 210300+1):
    if len(set(f(n))) == 4:
        print(*f(n))

"""
2 4 52561 105122
2 4 52567 105134
2 4 52571 105142
"""