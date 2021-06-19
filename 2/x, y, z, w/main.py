def F(y, w, z, x):
	return ((x <= y) and (y <= w)) or (z == (x or y))

print("y w z x F")
for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):
				if not F(y, w, z, x):
					print(y, w, z, x, 0)


# Ответ: xwzy