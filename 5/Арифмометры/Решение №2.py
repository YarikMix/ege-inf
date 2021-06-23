from itertools import product


def F(x, moves):
	for move in moves:
		if move == "1":
			x *= x
		elif move == "2":
			x += 1
	return x

for moves in product(("12"), repeat=4):
	if F(1, moves) == 17:
		print("".join(moves))
		break


# Ответ: 2112