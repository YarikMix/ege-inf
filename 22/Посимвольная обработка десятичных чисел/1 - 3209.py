def f(x):
	L = 0
	M = 0
	while x > 0:
	    L += 1
	    if x % 2 == 0:
	        M = M + (x % 10) // 2
	    x = x // 10
	return (L, M)

arr = [x for x in range(1, 1000) if f(x) == (3, 7)]
print(max(arr))

# Ответ: 986