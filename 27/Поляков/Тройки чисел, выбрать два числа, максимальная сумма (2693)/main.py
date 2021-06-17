with open("inputB.txt") as f:
	N = int(f.readline())
	s = [0]

	for _ in range(N):
		a, b, c = map(int, f.readline().split())
		pair = [a + b, a + c, b + c]
		combinations = [a + b for a in s for b in pair]
		s = {x % 4: x for x in sorted(combinations)}.values()

	m = max(x for x in s if x % 4 == 0)
	print(m)


# Ответ: 18380 58701760