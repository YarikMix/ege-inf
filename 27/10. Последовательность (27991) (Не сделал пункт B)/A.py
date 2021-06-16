# Решение только для A
from itertools import combinations


with open("inputA.txt") as f:
	arr = [int(i) for i in f.readlines()][1:]

	d = {}
	for x in combinations(arr, 2):
		if x[0] * x[1] % 17 == 0 and (x[0] - x[1]) % 2 == 0:
			d[sum(x)] = x

	max_sum = max(d.keys())
	pair = sorted(d[max_sum], reverse=True)
	print(*pair)

# A 8759, 3077