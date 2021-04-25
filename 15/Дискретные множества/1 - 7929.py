import time
from itertools import chain, combinations

def powerset(iterable):
    """powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))

P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}

def f(x, A):
	f = ((x in A) <= (x in P)) and ((x in Q) <= (x not in A))  
	return f

max_len = 0
for A in powerset(P | Q):
	OK = True
	for x in range(1, 1000):
		if not f(x, A):
			OK = False
			break
	if OK:
		max_len = max(max_len, len(A))

print(max_len)


# Ответ: 7