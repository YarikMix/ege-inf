with open("input.txt") as f:
	N, K, M = map(int, f.readline().split())
	arr = [int(f.readline()) for _ in range(N)]
	arr = sorted(arr)
	avg = sum(arr[0:K]) // K
	print(arr[-M], avg)

# arr[-M] - цена самого дешёвого смартфона премиум сегмента
# avg - целая часть средней цены телефона из бюджетного сегмента

# Ответ: 27700 7896