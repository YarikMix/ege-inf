def f(start, n):
	if n > start:
		return f(start, n - 1) + f(start, n - 3)
	elif n == start:
		return 1
	else:
		return 0

print(f(1, 9) * f(9, 17))  # 169