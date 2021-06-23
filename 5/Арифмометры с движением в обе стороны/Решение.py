from itertools import product


def F(x, moves):
	for move in moves:
		if move == "1":
			x -= 1
		elif move == "2":
			x *= 3
	return x

for moves in product(("12"), repeat=5):
	if F(3, moves) == 16:
		print("".join(moves))
		break


# Ответ: 12211