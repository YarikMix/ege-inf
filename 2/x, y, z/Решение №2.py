from itertools import product


def F(y, z, x):
	return (x == z) or (x <= (y and z))

print("y z x F")
for x, y, z in product((0, 1), repeat=3):
	if not F(y, z, x):
		print(y, z, x, 0)	


# Ответ: yzx