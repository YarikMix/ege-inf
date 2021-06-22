def DEL(n, m):
	return n % m == 0

def f(x, A):
	return DEL(x, A) or not DEL(x, 6) or not DEL(x, 4)

for A in range(1000, 1, -1):
	OK = True
	for x in range(1, 1000):
		OK *= f(x, A)
	if OK:
		print(A)
		break


# Ответ: 12