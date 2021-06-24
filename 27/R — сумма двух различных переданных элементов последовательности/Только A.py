from itertools import combinations


with open("inputA.txt") as f:
	arr = [int(i) for i in f.readlines()][1:]

	res = max(filter(lambda x: sum(x) % 3 == 0, combinations(arr, 2)))
	print(sum(res))


# Ответ: 19020