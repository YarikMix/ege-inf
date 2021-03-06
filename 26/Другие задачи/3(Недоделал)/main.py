with open("input.txt") as f:
	N, M = map(int, f.readline().split())
	arr = []
	for _ in range(N):
		s = f.readline().split(" ")
		arr.append({
			"price": int(s[0]),
			"count": int(s[1]),
			"type": s[2]
		})