def f(start, n):
	if n > start:
		if n % 2 == 0:
			return f(start, n - 1) + f(start, n - 2) + f(start, n // 2)
		else:
			return f(start, n - 1) + f(start, n - 2)
	elif n == start:
		return 1
	else:
		return 0

print(f(3, 10) * f(10, 12))  # 60