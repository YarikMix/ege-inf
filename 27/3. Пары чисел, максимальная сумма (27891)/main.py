# Решение №1
with open("inputB.txt") as f:
    # N - количество пар
    # min_diff - минимальная разница в парах, которая не делится на 5
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
        if x % 5 != 0:
            min_diff = min(min_diff, x)
            
    # Максимальная сумма
    if max_sum % 5 != 0:
        print(max_sum)
    else:
        """Если максимальная сумма делится на 5, то 
        уменьшаем ее на минимальную разницу в парах"""
        print(max_sum - min_diff)


# Решение №2
with open("inputB.txt") as f:
    N = int(f.readline())
    s = [0]

    for _ in range(N):
        pair = [int(x) for x in f.readline().split()]
        combination = [a + b for a in s for b in pair]
        s1 = [0] * 5
        for x in combination:
            s1[x % 5] = max(s1[x % 5], x)
        s = [x for x in s1 if x != 0]

    m = max(x for x in s if x % 5 != 0)
    print(m)


# Решение №3
with open("inputB.txt") as f:
    # N - количество пар
    N = int(f.readline())
    s = [0]

    for _ in range(N):
        pair = [int(x) for x in f.readline().split()]
        combination = [a + b for a in s for b in pair]
        s = {x % 5: x for x in sorted(combination)}.values()

    m = max(x for x in s if x % 5 != 0)
    print(m)


# Ответ: 118951 394491666