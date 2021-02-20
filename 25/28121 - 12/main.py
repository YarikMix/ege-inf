def is_prime(n):
    """Проверка числа на простоту"""
    d = 2
    while d*d <= n:
        if n % d == 0: return False
        d += 1
    return True
    

i = 1
for n in range(2422000, 2422080+1):
    if is_prime(n):
        print(f"{i} {n}")
        i += 1

"""
1 2422027
2 2422033
3 2422037
4 2422073
"""