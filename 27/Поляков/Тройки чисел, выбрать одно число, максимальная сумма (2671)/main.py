with open("inputB.txt") as f:
	N = int(f.readline())
	s = [0]

	for _ in range(N):
		pair = [int(x) for x in f.readline().split()]
		combinations = [a + b for a in s for b in pair]
		s = {x % 8: x for x in sorted(combinations)}.values()

	m = max(x for x in s if x % 8 == 0)
	print(m)


# Ответ: 14432 45978688