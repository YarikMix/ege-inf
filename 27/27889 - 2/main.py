with open("inputA.txt") as f:
    # N - количество пар
    # mindiff - минимальная разница в парах, которая не делится на 3
    # msum - минимальная сумма
    N, mindiff, msum = int(f.readline()), 10001, 0

    # Выбираем минимальные числа из пар
    for i in range(N):
        a, b = map(int, f.readline().split())
        msum += min(a, b)
        # Вычисляем минимальную разницу в парах
        x = abs(a - b)
        if x % 3 != 0 and x < mindiff:
            mindiff = x

    # Минимальная сумма
    if msum % 3 != 0:
        print(msum)
    else:
        """Если минимальная сумма делится на 3, то 
        уменьшаем ее на минимальную разницу в парах"""
        print(msum - mindiff)


# A 67088
# B 200157478 