def F(n):
    """Нахождение всех делителей числа, не считая единицы и самого числа."""
    arr = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            arr.extend([d, n // d])
        d += 1
    return sorted(arr)


def F(n):
    """Нахождение всех делителей числа"""
    arr = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            arr.extend([d, n // d])
        d += 1
    return sorted(arr)


def F(n):
    """Нахождение количества делителей числа"""
    count = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            count += 2
        d += 1
    return count


def F(n):
    """Возвращает  наибольший нетривиальный делитель числа,
    если число имеент ровно три нетривиальных делителя,
    в обратном случае возвращает False."""
    if int(n**0.25) == n**0.25 and is_prime(n**0.25):
        return int(n**0.75)
        

def is_prime(n):
    """Проверка числа на простоту"""
    d = 2
    while d*d <= n:
        if n % d == 0: return False
        d += 1
    return True