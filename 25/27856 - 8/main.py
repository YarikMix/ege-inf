def f(n):
    """Нахождение всех делителей числа"""
    arr = []
    d = 1
    while d*d <= n:
        if n % d == 0:
            arr.extend([d, n // d])
        d += 1
    return sorted(arr)
    
    
for n in range(95632, 95650+1):
    # Отбираем только различные нечётные делители
    arr = list(filter(lambda x: x % 2 == 1, set(f(n))))
    if(len(arr) == 6):
        print(*sorted(arr))

"""
1 3 9 10627 31881 95643
1 7 49 61 427 2989
1 5 25 1913 9565 47825
"""