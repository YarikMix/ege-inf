P = range(2, 10+1)
Q = range(6, 14+1)

def f(x, An, Ak):
	A = range(An, Ak+1)
	return ((x in A) <= (x in P)) or (x in Q)

max_len = 0
for An in range(1, 99):
	for Ak in range(An+1, 100):
		OK = True
		for x in range(1, 1000):
			if not f(x, An, Ak):
				OK = False
				break
		if OK:
			max_len = max(max_len, Ak - An)

print(max_len)


# Ответ: 12