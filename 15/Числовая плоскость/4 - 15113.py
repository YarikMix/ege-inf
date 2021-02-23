def f(x, y, A):
	f = ((x < A) <= (x * x < 100)) and ((y * y <= 64) <= (y <= A))
	return f

def main():
	res = 0
	for A in range(100):
		arr = [f(x, y, A) for x in range(200) for y in range(200)]
		if arr.count(True) == 40000:
			res += 1
	print(res)

main()  # 3