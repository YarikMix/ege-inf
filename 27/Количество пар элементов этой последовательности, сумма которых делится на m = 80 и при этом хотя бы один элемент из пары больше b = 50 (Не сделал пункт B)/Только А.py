from itertools import combinations


with open("inputA.txt") as f:
	arr = [int(i) for i in f.readlines()][1:]

	count = 0
	for x in combinations(arr, 2):
		if sum(x) % 80 == 0 and (x[0] > 50 or x[1] > 50):
			count += 1

	print(count)


# Ответ: 3