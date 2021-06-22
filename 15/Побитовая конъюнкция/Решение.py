def F(x, A):
	return x & 29 == 0 or x & 17 != 0 or x & A != 0

for A in range(1000):
	OK = all(F(x, A) for x in range(1000))
	if OK:
		print(A)
		break


# Ответ: 12