def F(N):
	a, b, c = map(int, str(N))
	return int("".join(map(str, sorted([a + b, b + c], reverse=True))))

N = 100
while F(N) != 1412:
	N += 1

print(N)


# Ответ: 395