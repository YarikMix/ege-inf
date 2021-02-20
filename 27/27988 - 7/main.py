with open("inputB.txt") as f:
    arr = [int(i) for i in f.readlines()][1:]

    # Max26 - максимальное число, кратное 26
    # Max13 - максимальное число, кратное 13, но не кратное 26
    # Max2 - максимальное число, кратное 2, но не кратное 26
    # Max - максимальное число, исключая Max26
    Max26 = max(filter(lambda x: x % 26 == 0, arr), default=0)
    Max13 = max(filter(lambda x: x % 13 == 0 and x % 26 != 0, arr), default=0)
    Max2 = max(filter(lambda x: x % 2 == 0 and x % 26 != 0, arr), default=0)
    Max = max(filter(lambda x: x != Max26, arr))

    X = max(Max26 * Max, Max13 * Max2)
    print(X)

# A 783900
# B 988000