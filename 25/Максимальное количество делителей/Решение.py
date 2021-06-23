def F(n):
    """Нахождение количества делителей числа"""
    count = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            count += 2
        d += 1
    return count

d = {F(n): n for n in range(84052, 84130+1)}
max_count = max(d.keys())
num = d[max_count]
print(max_count, num)


# Ответ: 72 84084