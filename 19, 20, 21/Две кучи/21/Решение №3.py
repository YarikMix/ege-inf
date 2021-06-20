from functools import lru_cache


def moves(h):
	a, b = h
	return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)

@lru_cache(None)
def game(h):
	a, b = h
	next = lambda *condition: (game(x) in condition for x in moves(h))
	if a + b >= 77:
		return "Win"
	elif any(next("Win")):
		return "Петя1"
	elif all(next("Петя1")):
		return "Ваня1"
	elif any(next("Ваня1")):
		return "Петя2"
	elif all(next("Петя1", "Петя2")):
		return "Ваня2"

print(min(S for S in range(1, 42) if game((7, S)) == "Ваня2"))


# Ответ: 30