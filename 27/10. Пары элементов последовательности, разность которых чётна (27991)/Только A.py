from itertools import combinations


with open("inputA.txt") as f:
	arr = [int(i) for i in f.readlines()][1:]

	d = {}
	for a, b in combinations(arr, 2):
		if a * b % 17 == 0 and (a - b) % 2 == 0:
			d[a + b] = (a, b)

	max_sum = max(d.keys())
	print(*d[max_sum])


# Ответ: 3077 8759