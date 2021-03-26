def is_square(n):
    return n**0.5 == int(n**0.5)

def is_prime(n):
	d = 2
	while d * d <= n:
		if n % d == 0:
			return False
		d += 1
	return True

for n in range(101 * 10 ** 6 , 102 * 10 ** 6 + 1, 2):
	if is_square(n // 2) and is_prime((n // 2) ** 0.5):
		print(n)


"""
Ответ:
101075762
101417282
101588258
101645282
"""