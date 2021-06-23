def DEL(n, m):
	return n % m == 0

def F(x, A):
	return (DEL(x, A) and DEL(x, 12)) <= (DEL(x, 42) or not DEL(x, 12))

for A in range(1, 1000):
	OK = all(F(x, A) for x in range(1, 1000))
	if OK:
		print(A)
		break


# Ответ: 7