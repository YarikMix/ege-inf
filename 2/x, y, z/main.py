def F(y, z, x):
	return (x is z) or (x <= (y and z))

print("y z x F")
for x in range(2):
	for y in range(2):
		for z in range(2):
			if not F(y, z, x):
				print(y, z, x, 0)


# Ответ: yzx