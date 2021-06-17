# Решение №1
with open("inputA.txt") as f:
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


# Решение №2
with open("inputA.txt") as f:
    # N - количество пар
    N = int(f.readline())
    s = [0]

    for _ in range(N):
        pair = [int(x) for x in f.readline().split()]
        combination = [a + b for a in s for b in pair]
        s1 = [0] * 3
        for x in combination:
            s1[x % 3] = max(s1[x % 3], x)
        s = [x for x in s1 if x != 0]

    m = max(x for x in s if x % 3 != 0)
    print(m)


# Решение №3
with open("inputA.txt") as f:
    # N - количество пар
    N = int(f.readline())
    s = [0]

    for _ in range(N):
        pair = [int(x) for x in f.readline().split()]
        combination = [a + b for a in s for b in pair]
        s = {x % 3: x for x in sorted(combination, reverse=True)}.values()

    m = min(x for x in s if x % 3 != 0)
    print(m)


# Ответ: 67088 200157478