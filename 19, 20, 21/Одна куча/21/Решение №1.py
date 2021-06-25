from functools import lru_cache


def moves(h):
	return h + 1, h + 3, h * 2

@lru_cache(None)
def game(h):
	if h >= 42:
		return "Победа"
	elif any(game(x) == "Победа" for x in moves(h)):
		return "Петя1"
	elif all(game(x) == "Петя1" for x in moves(h)):
		return "Ваня1"
	elif any(game(x) == "Ваня1" for x in moves(h)):
		return "Петя2"
	elif all(game(x) == "Петя1" or game(x) == "Петя2" for x in moves(h)):
		return "Ваня2"

print(min(S for S in range(1, 42) if game(S) == "Ваня2"))


# Ответ: 16