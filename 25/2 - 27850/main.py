def is_prime(n):
    """Проверка числа на простоту"""
    d = 2
    while d*d <= n:
        if n % d == 0: return False
        d += 1
    return True

r = range(245690, 245756+1)
for i, n in enumerate(r, start=1):
    if is_prime(n):
        print(f"{i} {n}")

"""
22 245711
30 245719
34 245723
52 245741
58 245747
64 245753
"""