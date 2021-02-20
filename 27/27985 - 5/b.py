with open("inputB.txt") as f:
    arr = [int(i) for i in f.readlines()][1:]

    # Max14 - максимальное число, кратное 14
    # Max7 - максимальное число, кратное 7, но не кратное 14
    # Max2 - максимальное число, кратное 2, но не кратное 14
    # Max - максимальное число, исключая Max14
    Max14 = max(filter(lambda x: x % 14 == 0, arr), default=0)
    Max7 = max(filter(lambda x: x % 7 == 0 and x % 14 != 0, arr), default=0)
    Max2 = max(filter(lambda x: x % 2 == 0 and x % 14 != 0, arr), default=0)
    Max = max(filter(lambda x: x != Max14, arr))

    R = max(Max14 * Max, Max7 * Max2)
    print(R)

# A 719740
# B 994000