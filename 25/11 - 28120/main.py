def f(n):
    """Нахождение всех делителей числа"""
    arr = []
    d = 1
    while d*d <= n:
        if n % d == 0:
            arr.extend([d, n // d])
        d += 1
    return sorted(arr)
    
    
for n in range(201455, 201470+1):
    if len(set(f(n))) == 4:
        print(*f(n))

"""
1 3 67153 201459
1 13 15497 201461
1 29 6947 201463
1 2 100733 201466
"""