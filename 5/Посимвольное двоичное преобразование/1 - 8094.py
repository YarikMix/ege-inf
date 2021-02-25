def g(s):
	"""Возвращает остаток от деления суммы цифр на 2"""
	return str(sum([int(i) for i in s]) % 2)

def f(N):
	"""Алгоритм из условия задачи"""
	R = format(N, "b")
	R += g(R)
	R += g(R)
	return int(R, 2)

# for N in range(1, 100):
# 	print(f"N = {N}, R = {f(N)}")

arr = [f(N) for N in range(1, 100)]
arr = list(filter(lambda x: x > 43, arr))
print(min(arr))  # 46