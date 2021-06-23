for N in range(200000000, 400000000+1):
	if N % 12 == 0:
		for m in range(2, 31, 2):
			for n in range(1, 21, 2):
				if N == (2 ** m) * (3 ** n):
					print(N)