with open("inputA.txt") as f:
    N = int(f.readline())
    arr = [int(f.readline()) for _ in range(N)]

    n62 = len(list(filter(lambda x: x % 62 == 0, arr)))
    n31 = len(list(filter(lambda x: x % 31 == 0 and x % 62 != 0, arr)))
    n2 = len(list(filter(lambda x: x % 2 == 0 and x % 62 != 0, arr)))

    count = n62 * (n62 - 1) / 2 + n62 * (N - n62) + n2 * n31
    print(int(count))

# A 0
# B 82307095