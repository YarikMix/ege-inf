def f(n):
    """Нахождение всех делителей числа"""
    arr = []
    d = 1
    while d*d <= n:
        if n % d == 0:
            arr.extend([d, n // d])
        d += 1
    return sorted(arr)

    
for n in range(185311, 185330+1):
    if len(set(f(n))) == 4:
        print(*f(n))

"""
1 2 92657 185314
1 47 3943 185321
1 241 769 185329
"""