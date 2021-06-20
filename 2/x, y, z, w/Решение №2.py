from itertools import product


def F(y, w, z, x):
	return ((x <= y) and (y <= w)) or (z == (x or y))

print("y w z x F")
for x, y, z, w in product((0, 1), repeat=4):
	if not F(y, w, z, x):
		print(y, w, z, x, 0)	


# Ответ: ywzx