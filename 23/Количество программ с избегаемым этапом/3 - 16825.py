def f(start, n):
	if n > start and n not in (6, 12):
		if n % 2 == 0:
			# Если n делится на 2
			return f(start, n - 1) + f(start, n - 3) + f(start, n // 2)
		else: 
			# Если n не делится на 2
			return f(start, n - 1) + f(start, n - 3)
	elif n == start:
		return 1
	else:
		return 0

print(f(3, 16))  # 22