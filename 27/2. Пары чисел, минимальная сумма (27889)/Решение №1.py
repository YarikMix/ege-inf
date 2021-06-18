with open("inputB.txt") as f:
    # N - количество пар
    # min_diff - минимальная разница в парах, которая не делится на 3
    # min_sum - минимальная сумма
    N = int(f.readline())
    min_diff = 10001
    min_summ = 0

    # Выбираем минимальные числа из пар
    for i in range(N):
        a, b = map(int, f.readline().split())
        min_summ += min(a, b)
        # Вычисляем минимальную разницу в парах
        x = abs(a - b)
        if x % 3 != 0:
            min_diff = min(min_diff, x)

    # Минимальная сумма
    if min_summ % 3 != 0:
        print(min_summ)
    else:
        """Если минимальная сумма делится на 3, то 
        уменьшаем ее на минимальную разницу в парах"""
        print(msum - min_diff)


# Ответ: 67088 200157478