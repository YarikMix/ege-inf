def F(x, y, i=0, moves=""):
	if i > 4:
		return 0
	elif i == 4:
		print(moves)
	else:
		if x == y:
			print(moves)
		elif x < y:
			return F(x * x, y, i + 1, moves + "1"), F(x + 1, y, i + 1, moves + "2")
		else:
			return 0

F(1, 17)


# Ответ: 2112