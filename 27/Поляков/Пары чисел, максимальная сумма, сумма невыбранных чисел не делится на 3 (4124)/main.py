with open("inputA.txt") as f:
    N = int(f.readline())
    s = [0]
    S = 0

    for _ in range(N):
        pair = [int(x) for x in f.readline().split()]
        S += sum(pair)
        combinations = [a + b for a in s for b in pair]
        s = {x % 15: x for x in sorted(combinations)}.values()

    m = max(x for x in s if x % 5 != 0 and (S - x) % 3 != 0)
    print(m)


# Ответ: 453 3695118