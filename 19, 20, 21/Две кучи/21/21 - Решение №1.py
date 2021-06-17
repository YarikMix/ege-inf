N1 = 7
end = 77
lose = []
output = [[0] * 2 * end for _ in range(2 * end)]

for x in range(end - 1, 0, -1):
	for y in range(end- x - 1, 0, -1):
		follow = [output[x + 1][y], output[2 * x][y], 
			      output[x][y + 1], output[x][2 * y]]
		lose = [follow[i] for i in range(4) if follow[i] <= 0]
		if lose:
			output[x][y] = -max(lose) + 1
		else:
			output[x][y] = -max(follow)

print(min([S for S in range(1, end - N1 + 1) if output[N1][S] == -2]))


# Ответ: 30