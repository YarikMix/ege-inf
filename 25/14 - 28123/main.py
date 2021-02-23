def f(n):
    """Нахождение всех делителей числа"""
    arr = []
    d = 1
    while d*d <= n:
        if n % d == 0:
            arr.extend([d, n // d])
        d += 1
    return sorted(arr)

    
for n in range(125256, 125330+1):
    # Отбираем только различные чётные делители
    arr = list(filter(lambda x: x % 2 == 0, set(f(n))))
    if(len(arr) == 6):
        print(*sorted(arr))

"""
2 6 18 13918 41754 125262
2 4 8 31322 62644 125288
2 6 18 13922 41766 125298
"""