with open("inputB.txt") as f:
    N = int(f.readline())
    arr = [int(f.readline()) for _ in range(N)]

    # Max26 - максимальное число, кратное 26
    # Max13 - максимальное число, кратное 13, но не кратное 26
    # Max2 - максимальное число, кратное 2, но не кратное 26
    # Max - максимальное число, исключая Max26
    Max26 = max(filter(lambda x: x % 26 == 0, arr), default=0)
    Max13 = max(filter(lambda x: x % 13 == 0 and x % 26 != 0, arr), default=0)
    Max2 = max(filter(lambda x: x % 2 == 0 and x % 26 != 0, arr), default=0)
    Max = max(filter(lambda x: x != Max26, arr))

    R = max(Max26 * Max, Max13 * Max2)
    print(R)


# Ответ: 783900 988000