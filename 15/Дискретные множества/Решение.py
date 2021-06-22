from itertools import chain, combinations


def powerset(iterable):
    """powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))

P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}

def F(x, A):
	return ((x in A) <= (x in P)) and ((x in Q) <= (x not in A))  

max_len = 0
for A in powerset(P | Q):
	OK = all(F(x, A) for x in range(1000))
	if OK:
		max_len = max(max_len, len(A))

print(max_len)


# Ответ: 7