from functools import lru_cache


def moves(h):
	return h + 1, h + 3, h * 2

@lru_cache(None)
def game(h):
	if h >= 42:
		return "Победа"
	elif any(game(x) == "Победа" for x in moves(h)):
		return "Петя1"
	elif any(game(x) == "Петя1" for x in moves(h)):
		return "Ваня1"

print(min(S for S in range(1, 42) if game(S) == "Ваня1"))


# Ответ: 11