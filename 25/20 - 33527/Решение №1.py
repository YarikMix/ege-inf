def f(n):
	d = 2
	k = 1
	while d * d < n:
		if n % d == 0:
			if d % 2 == 0:
				k += 1
			if n // d % 2 == 0:
				k += 1
			if k > 3:
				return k
		d += 1
	if d * d == n:
		k += 1
	return k

for n in range(101*10**6, 102*10**6+1):
	if n % 2 == 0:
		if f(n) == 3:
			print(n)


"""
Ответ:
101075762
101417282
101588258
101645282
"""