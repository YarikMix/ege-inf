def F(x, y, A):
	return ((x <= 9) <= (x * x <= A)) and ((y * y <= A) <= (y <= 9))

for A in range(1000, 1, -1):
	OK = all(F(x, y, A) for x in range(1000) for y in range(1000))
	if OK:
		print(A)
		break


# Ответ: 99