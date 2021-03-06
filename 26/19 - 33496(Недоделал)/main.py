# Решение №1
with open("input.txt") as f:
	N, M = map(int, f.readline().split())
	arr, res = [], []

	# Все грузы весом от 210 до 220 кг помещаем в список res
	# Остальные грузы помещаем в список arr
	for _ in range(N):
		cargo = int(f.readline())
		res.append(cargo) if 210 <= cargo <= 220 else arr.append(cargo)

	arr.sort()
	res.sort()		

	for i in range(len(arr)-1):
		if sum(res) + arr[i] <= M:
			res.append(arr[i])
		elif sum(res) - arr[i-1] + arr[i] <= M:
			del(res[-1])
			res.append(arr[i])
		elif sum(res) - arr[i-1] - arr[i] + arr[i+1] <= M:
			del(res[-1])
			res.append(arr[i+1])
		else:
			break
	print(len(res), sum(res) + 1)


# Решение №2
with open("input.txt") as f:
	N, M = map(int, f.readline().split())
	arr = [int(f.readline()) for _ in range(N)]
	# В итоговый список забираем все грузы, массой от 210кг до 220кг
	res = sorted(list(filter(lambda x: 210 <= x <= 220, arr)))
	# Исключаем из первоначального списка все грузы, массой от 210кг до 220кг
	arr = sorted(list(filter(lambda x: x < 210 or x > 220, arr)))

	for i in range(len(arr)-1):
		if sum(res) + arr[i] <= M:
			res.append(arr[i])
		elif sum(res) - arr[i-1] + arr[i] <= M:
			del(res[-1])
			res.append(arr[i])
		else:
			break
	print(len(res), sum(res) + 1)


# Ответ: 122 10000