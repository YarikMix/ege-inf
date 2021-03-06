# 25 задача
Задача связана с перебором и делимостью<br>
Нужно найти числа, удовлетворяющие некоторому условию

## Полезные функции

### Нахождение всех делителей числа, не считая единицы и самого числа
```bash
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
```

### Нахождение всех делителей числа
```bash
def f(n):
    """Нахождение всех делителей числа"""
    arr = []
    d = 1
    while d*d <= n:
        if n % d == 0:
            arr.extend([d, n // d])
        d += 1
    return sorted(arr)
```

### Проверка числа на простоту
```bash
def is_prime(n):
    """Проверка числа на простоту"""
    d = 2
    while d*d <= n:
        if n % d == 0: return False
        d += 1
    return True
```

### Работа с нетривиальными делителями
```bash
def f(n):
    """Возвращает  наибольший нетривиальный делитель числа,
    если число имеент ровно три нетривиальных делителя,
    в обратном случае возвращает False."""
    if int(n**0.25) == n**0.25 and is_prime(n**0.25):
        return int(n**0.75)
```

Все функции работают за O(n²), благодаря перебору до корня из числа. Иначе, в некоторых заданиях, программе не хватит времени