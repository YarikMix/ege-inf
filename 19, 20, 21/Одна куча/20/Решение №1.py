from functools import lru_cache


def moves(h):
	return h + 1, h + 3, h * 2

@lru_cache(None)
def game(h):
	def next(*condition):
		return (game(x) in condition for x in moves(h))
	if h >= 42: return "Победа"
	elif any(next("Победа")): return "Петя1"
	elif all(next("Петя1")): return "Ваня1"
	elif any(next("Ваня1")): return "Петя2"

print(*(S for S in range(1, 42) if game(S) == "Петя2"))


# Ответ: 10 17 19