from functools import lru_cache


def moves(h):
	return h + 1, h + 3, h * 2

@lru_cache(None)
def game(h):
	if h >= 42:
		return "Win"
	elif any(game(m) == "Win" for m in moves(h)):
		return "Петя1"
	elif all(game(m) == "Петя1" for m in moves(h)):
		return "Ваня1"
	elif any(game(m) == "Ваня1" for m in moves(h)):
		return "Петя2"
	elif all(game(m) == "Петя1" or game(m) == "Петя2" for m in moves(h)):
		return "Ваня2"

print(min([S for S in range(1, 42) if game(S) == "Ваня2"]))


# Ответ: 16