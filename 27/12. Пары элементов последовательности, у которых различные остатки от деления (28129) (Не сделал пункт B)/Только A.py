from itertools import combinations


with open("inputA.txt") as f:
	arr = [int(i) for i in f.readlines()][1:]

	d = {}
	for a, b in combinations(arr, 2):
		if a % 160 != b % 160 and (a * b) % 7 == 0:
			d[a + b] = (a, b)

	max_sum = max(d.keys())
	print(*d[max_sum])


# Ответ: 728 977