def f(n):
    """Нахождение всех делителей числа"""
    arr = []
    d = 1
    while d*d <= n:
        if n % d == 0:
            arr.extend([d, n // d])
        d += 1
    return sorted(arr)

    
for n in range(312614, 312651+1):
    if len(set(f(n))) == 6:
        print(*f(n))

"""
1 2 4 78157 156314 312628
1 3 9 34739 104217 312651
"""