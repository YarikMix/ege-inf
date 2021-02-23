def DEL(x, A):
	"""Возвращает True, если x делится на A,
	иначе возвращает False."""
	return x % A == 0

def f(x, A):
	f = DEL(x, A) or not DEL(x, 6) or not DEL(x, 9)
	return f

def main():
	for A in range(1, 1000):
		arr = [f(x, A) for x in range(1, 1000)]
		if arr.count(True) == 999:
			print(A)

main()  # 18