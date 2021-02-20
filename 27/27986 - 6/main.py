with open("inputB.txt") as f:
    arr = [int(i) for i in f.readlines()][:-1]

    # Max7 - максимальное число, кратное 7, но не кратное 49
    # Max - максимальное число, не кратное 7
    Max7 = max(filter(lambda x: x % 7 == 0 and x % 49 != 0, arr), default=0)
    Max = max(filter(lambda x: x % 7 != 0, arr), default=0)

    print(Max7 * Max)

# A 816130
# B 994000