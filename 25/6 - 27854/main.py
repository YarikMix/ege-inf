def f(n):
    """Нахождение всех делителей числа"""
    arr = []
    d = 1
    while d*d <= n:
        if n % d == 0:
            arr.extend([d, n // d])
        d += 1
    return sorted(arr)

    
for n in range(110203, 110245+1):
    # Отбираем только различные чётные делители
    arr = list(filter(lambda x: x % 2 == 0, set(f(n))))
    if(len(arr) == 4):
        print(*sorted(arr))

"""
2 4 55102 110204
2 14 15746 110222
2 6 36742 110226
2 22 10022 110242
"""