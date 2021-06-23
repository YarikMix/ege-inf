def G(s):
	"""Возвращает остаток от деления суммы цифр на 2"""
	return str(sum([int(i) for i in s]) % 2)

def F(N):
	R = format(N, "b")
	R += G(R)
	R += G(R)
	return int(R, 2)

N = 1
while F(N) <= 43:
	N += 1

print(F(N))


# Ответ: 46