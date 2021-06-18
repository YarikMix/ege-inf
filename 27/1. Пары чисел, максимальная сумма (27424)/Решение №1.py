with open("inputB.txt") as f:
    # N - количество пар
    # min_diff - минимальная разница в парах, которая не делится на 3
    # max_sum - максимальная сумма
    N = int(f.readline())
    min_diff = 10001
    max_sum = 0

    # Выбираем максимальные числа из пар
    for _ in range(N):
        a, b = map(int, f.readline().split())
        max_sum += max(a, b)
        # Вычисляем минимальную разницу в парах
        x = abs(a - b)
        if x % 3 != 0:
            min_diff = min(min_diff, x)
            
    # Максимальная сумма
    if max_sum % 3 != 0:
        print(max_sum)
    else:
        """Если максимальная сумма делится на 3, то 
        уменьшаем ее на минимальную разницу в парах"""
        print(max_sum - min_diff)


# Ответ: 127127 399762080