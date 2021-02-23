# Решение только для A
with open("inputA.txt") as f:
	n = int(f.readline())
	arr = [int(f.readline()) for i in range(n)]

	d = {}
	for i in range(n):
		for j in range(n):
			if i < j and arr[i] > arr[j] and (arr[i] + arr[j]) % 120 == 0:
				d[arr[i] + arr[j]] = (arr[i], arr[j])

	max_sum = max(d.keys())
	pair = d[max_sum]
	print(*pair)

# A 8096, 6544