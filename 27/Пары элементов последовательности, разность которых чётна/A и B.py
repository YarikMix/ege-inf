with open("inputB.txt") as f:
	p = 17
	m0 = m1 = mp0 = mp1 = 0
	N = int(f.readline())
	for i in range(N):
	    a = int(f.readline())
	    if a % 2 == 0:
	        if a % p == 0 and a >= mp0:
	            if mp0 > m0: m0 = mp0
	            mp0 = a
	        elif a > m0: m0 = a
	    else:
	        if a % p == 0 and a >= mp1:
	            if mp1 > m1: m1 = mp1
	            mp1 = a
	        elif a > m1: m1 = a
	x = y = 0
	if mp0 > 0 and m0 > 0:
	    x = mp0; y = m0
	if mp1 > 0 and m1 > 0 and mp1 + m1 > x + y:
	    x = mp1; y = m1
	print(x,y)


# Ответ: A) 3077 8759 B) 9996 10000