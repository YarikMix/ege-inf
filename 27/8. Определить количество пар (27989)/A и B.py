with open("inputB.txt") as f:
    N = int(f.readline())
    arr = [int(f.readline()) for _ in range(N)]

    n26 = len(list(filter(lambda x: x % 26 == 0, arr)))
    n13 = len(list(filter(lambda x: x % 13 == 0 and x % 26 != 0, arr)))
    n2 = len(list(filter(lambda x: x % 2 == 0 and x % 26 != 0, arr)))

    count = n26 * (n26 - 1) // 2 + n26 * (N - n26) + n2 * n13
    print(count)


# Ответ: 19 199360639