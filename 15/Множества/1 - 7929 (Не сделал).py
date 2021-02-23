P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}

def f(x, An, Ak):
	A = range(An, Ak + 1)
	f = ((x in A) <= (x in P)) and (not(x in Q) or (x in A))  
	return f

def main():
	max_lenght = 0
	for An in range(1, 100):
		for Ak in range(An, 100):
			arr = [f(x, An, Ak) for x in range(1000)]
			if arr.count(True) == 1000:
				max_lenght = max(max_lenght, Ak - An)
	print(max_lenght)

main()