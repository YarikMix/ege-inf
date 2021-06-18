with open("inputB.txt") as f:
    N = int(f.readline())
    s = [0]

    for _ in range(N):
        pair = [int(x) for x in f.readline().split()]
        combination = [a + b for a in s for b in pair]
        s = {x % 3: x for x in sorted(combination, reverse=True)}.values()

    m = min(x for x in s if x % 3 != 0)
    print(m)


# Ответ: 67088 200157478