def f(n):
    """Нахождение всех делителей числа"""
    arr = []
    d = 1
    while d*d <= n:
        if n % d == 0:
            arr.extend([d, n // d])
        d += 1
    return sorted(arr)

    
for n in range(489421, 489440+1):
    if len(set(f(n))) == 4:
        print(*f(n))

"""
1 19 25759 489421
1 2 244711 489422
1 13 37649 489437
"""