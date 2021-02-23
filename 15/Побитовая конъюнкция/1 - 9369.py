def f(x, A):
	f = x & 25 == 0 or x & 17 != 0 or x & A != 0
	return f

def main():
	for A in range(0, 1000):
		arr = [f(x, A) for x in range(0, 1000)]
		if arr.count(True) == 1000:
			return A

print(main())  # 8