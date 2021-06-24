with open("inputA.txt") as f:
	n = int(f.readline())
	y = [0] * 160
	z7 = [0] * 160
	smax = 0
	s1 = s2 = 0
	for i in range(n):
		x = int(f.readline())
		p = x % 160
		t = 0
		if x % 7 == 0:
			for j in range(160):
				if j != p and y[j] > t:
					t = y[j]
			if x > z7[p]:
				z7[p] = x
		else:
			for j in range(160):
				if j != p and z7[j] > t:
					t = z7[j]
	if t > 0 and x + t > smax:
		smax = x + t
		s1 = x
		s2 = t
	if x > y[p]:
		y[p] = x
	print(s1, s2)


# Ответ: 310 728