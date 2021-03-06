"""
Задача про спутник "Фотон"
"""

with open("input.txt") as f:
	N, K = map(int, f.readline().split())
	arr = [int(f.readline()) for _ in range(N)]

arr.sort()
arr = arr[K:N-K]
avg = sum(arr) // len(arr)
print(max(arr), avg)

# Ответ: 957 501