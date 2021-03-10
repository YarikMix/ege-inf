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

	for product in filter(lambda x: x["type"] == "B", arr):
		M -= product["price"] * product["count"]

	print(M)  # 1425146

	count = 0
	for product in filter(lambda x: x["type"] == "A", arr):
		if M - product["price"] * product["count"] > 0:
			M -= product["price"] * product["count"]
			count += 1

	print(count)
	print(M)

# Ответ: 140 789