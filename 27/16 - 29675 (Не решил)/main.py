with open("inputA.txt") as f:
    # N - количество пар,
    # mindiff - минимальная разница в парах, которая не делится на 3,
    # msum - максимальная сумма
    N, mindiff, msum = int(f.readline()), 10001, 0

    # Выбираем максимальные числа из пар
    for i in range(N):
        a, b = map(int, f.readline().split())
        msum += max(a, b)
        # Вычисляем минимальную разницу в парах
        x = abs(a - b)
        if x % 3 == 0 and x < mindiff:
            mindiff = x
            
    # Максимальная сумма
    if msum % 3 == 0:
        print(msum)
    else:
        """Если максимальная сумма не делится на 3, то 
        уменьшаем ее на минимальную разницу в парах"""
        print(msum - mindiff)

# A 125570 - Неправильный ответ
# B 399759476 - Неправильный ответ 