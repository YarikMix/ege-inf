with open("inputB.txt") as f:
    N = int(f.readline())
    arr = [int(f.readline()) for _ in range(N)]

    # Max14 - максимальное число, кратное 14
    # Max7 - максимальное число, кратное 7, но не кратное 14
    # Max2 - максимальное число, кратное 2, но не кратное 14
    # Max - максимальное число, исключая Max14
    Max14 = max(filter(lambda x: x % 14 == 0, arr), default=0)
    Max7 = max(filter(lambda x: x % 7 == 0 and x % 14 != 0, arr), default=0)
    Max2 = max(filter(lambda x: x % 2 == 0 and x % 14 != 0, arr), default=0)
    Max = max(filter(lambda x: x != Max14, arr))

    X = max(Max14 * Max, Max7 * Max2)
    print(X)


# Ответ: 447552 994000