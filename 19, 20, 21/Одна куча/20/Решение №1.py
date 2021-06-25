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

print(*(S for S in range(1, 42) if game(S) == "Петя2"))


# Ответ: 10 17 19