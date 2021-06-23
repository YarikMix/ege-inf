from functools import lru_cache


def moves(h):
	a, b = h
	return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)

@lru_cache(None)
def game(h):
	if sum(h) >= 77:
		return "Win"
	elif any(game(x) == "Win" for x in moves(h)):
		return "Петя1"
	elif all(game(x) == "Петя1" for x in moves(h)):
		return "Ваня1"
	elif any(game(x) == "Ваня1" for x in moves(h)):
		return "Петя2"
	elif all(game(x) == "Петя1" or game(x) == "Петя2" for x in moves(h)):
		return "Ваня2"

print(min(S for S in range(1, 42) if game((7, S)) == "Ваня2"))


# Ответ: 30