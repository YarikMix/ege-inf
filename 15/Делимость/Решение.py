def DEL(n, m):
	return n % m == 0

def F(x, A):
	return DEL(x, A) or not DEL(x, 6) or not DEL(x, 4)

for A in range(1000, 1, -1):
	OK = all(F(x, A) for x in range(1000))
	if OK:
		print(A)
		break


# Ответ: 12