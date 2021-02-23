def f(x, y, A):
	f = ((x <= 9) <= (x * x <= A)) and ((y * y <= A) <= (y <= 9))
	return f

def main():
	for A in range(1000):
		arr = [f(x, y, A) for x in range(100) for y in range(100)]
		if arr.count(True) == 10000:
			print(A)

main()  # 99