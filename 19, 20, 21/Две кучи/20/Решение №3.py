from functools import lru_cache


def moves(h):
	a, b = h
	return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)

@lru_cache(None)
def game(h):
	next = lambda *condition: (game(x) in condition for x in moves(h))
	if sum(h) >= 77: return "Победа"
	elif any(next("Победа")): return "Петя1"
	elif all(next("Петя1")): return "Ваня1"
	elif any(next("Ваня1")): return "Петя2"

print(*(S for S in range(1, 42) if game((7, S)) == "Петя2"))


# Ответ: 31 34