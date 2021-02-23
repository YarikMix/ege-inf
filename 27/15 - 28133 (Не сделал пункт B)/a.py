# Решение только для A
with open("inputA.txt") as f:
	N = int(f.readline())
	arr = [int(f.readline()) for i in range(N)]

	d = {}
	for i in range(N):
		for j in range(N):
			if arr[i] > arr[j] and i < j <= N and (arr[i] + arr[j]) % 120 == 0:
				d[arr[i] + arr[j]] = (arr[i], arr[j])

	try:
		max_sum = max(d.keys())
		pair = d[max_sum]
		print(*pair)
	except:
		print("00")

# A 00