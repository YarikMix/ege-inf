for n in range(1000000, 2000000+1):
	k = 0
	d = 1
	while d * d <= n:
		if n % d == 0:
			if n // d - d <= 100:
				k += 1
			if k == 3:
				print(n)
				break
		d += 1


"""
Ответ:
1113840
1179360
1208844
1499400
"""