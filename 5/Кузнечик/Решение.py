from itertools import product


def F(x, moves):
	for move in moves:
		if move == "1":
			x += 5
		elif move == "2":
			x -= 3
	return x

for moves in product(("12"), repeat=9):
	if F(0, moves) == 21:
		print("".join(moves).count("2"))
		break


# Ответ: 3