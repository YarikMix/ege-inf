P = range(5, 30+1)
Q = range(14, 23+1)

def f(x, An, Ak):
	A = range(An, Ak + 1)
	f = ((x in P) != (x in Q)) or not(x in A)
	return f

def main():
	max_lenght = 0
	for An in range(100):
		for Ak in range(An, 100):
			arr = [f(x, An, Ak) for x in range(1000)]
			if arr.count(True) == len(arr):
				max_lenght = max(max_lenght, Ak - An)
	print(max_lenght + 1)

main()


# Ответ: 9