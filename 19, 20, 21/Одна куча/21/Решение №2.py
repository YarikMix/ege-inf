from functools import lru_cache


def moves(h):
	return h + 1, h + 3, h * 2

@lru_cache(None)
def game(h):
	next = lambda *condition: (game(x) in condition for x in moves(h))
	if h >= 42:
		return "Win"
	elif any(next("Win")):
		return "Петя1"
	elif all(next("Петя1")):
		return "Ваня1"
	elif any(next("Ваня1")):
		return "Петя2"
	elif all(next("Петя1", "Петя2")):
		return "Ваня2"

print(min(S for S in range(1, 42) if game(S) == "Ваня2"))


# Ответ: 16