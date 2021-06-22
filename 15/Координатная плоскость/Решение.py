def F(x, y, A):
	return ((x <= 9) <= (x * x <= A)) and ((y * y <= A) <= (y <= 9))

for A in range(1000, 1, -1):
	OK = True
	for x in range(100):
		for y in range(100):
			OK *= F(x, y, A)
	if OK:
		print(A)
		break


# Ответ: 99