def f(n):
    """Нахождение всех делителей числа"""
    arr = []
    d = 1
    while d*d <= n:
        if n % d == 0:
            arr.extend([d, n // d])
        d += 1
    return sorted(arr)
    
    
for n in range(95632, 95700+1):
    # Отбираем только различные чётные делители
    arr = list(filter(lambda x: x % 2 == 0, set(f(n))))
    if(len(arr) == 6):
        print(*sorted(arr))

"""
2 10 50 3826 19130 95650
2 26 338 566 7358 95654
2 4 8 23918 47836 95672
"""