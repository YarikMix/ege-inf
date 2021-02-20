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


def f(n):
    """Нахождение всех делителей числа"""
    arr = []
    d = 1
    while d*d <= n:
        if n % d == 0:
            arr.extend([d, n // d])
        d += 1
    return sorted(arr)


def is_prime(n):
    """Проверка числа на простоту"""
    d = 2
    while d*d <= n:
        if n % d == 0: return False
        d += 1
    return True


def f(n):
    """Возвращает  наибольший нетривиальный делитель числа,
    если число имеент ровно три нетривиальных делителя,
    в обратном случае возвращает False."""
    arr = []
    k = 0
    d = 2
    if int(n**0.25) == n**0.25:
        while d*d < n:
            if n % d == 0:
                arr.extend([d, n // d])
                k += 2
                if k > 3: return False
            d += 1
        if d*d == n: k += 1
        if k == 3: return max(arr)