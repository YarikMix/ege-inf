from functools import lru_cache


def moves(h):
	a, b = h
	return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)

@lru_cache(None)
def game(h):
	if sum(h) >= 77:
		return "Win"
	elif any(game(m) == "Win" for m in moves(h)):
		return "Петя1"
	elif any(game(m) == "Петя1" for m in moves(h)):
		return "Ваня1"

print(min(S for S in range(1, 42) if game((7, S)) == "Ваня1"))


# Ответ: 18