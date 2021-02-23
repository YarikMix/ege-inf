def DEL(x, A):
	"""Возвращает True, если x делится на A,
	иначе возвращает False."""
	return x % A == 0

def f(x, A):
	f = (A < 50) and (DEL(x, A) or not DEL(x, 10) or not DEL(x, 12))
	return f

def main():
	for A in range(1, 100):
		arr = [f(x, A) for x in range(1, 100)]
		if arr.count(True) == 99:
			print(A)

main()  # 30