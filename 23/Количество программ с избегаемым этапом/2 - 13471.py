def f(start, n):
	if n > start and n != 24:
		if n % 2 == 1:
			# Если n нечётное
			return f(start, n - 1) + f(start, (n - 1) // 2)
		else: 
			# Если n чётное
			return f(start, n - 1) 
	elif n == start:
		return 1
	else:
		return 0

print(f(1, 25))  # 10