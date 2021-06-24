with open("inputB.txt") as f:
    N = int(f.readline())
    s = [0]

    for _ in range(N):
        pair = [int(x) for x in f.readline().split()]
        combination = [a + b for a in s for b in pair]
        s = {x % 3: x for x in sorted(combination)}.values()

    m = max(x for x in s if x % 3 != 0)
    print(m)


# Ответ: 127127 399762080