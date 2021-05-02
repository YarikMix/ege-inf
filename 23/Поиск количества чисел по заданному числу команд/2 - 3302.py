arr = []
def f(x, i=0):
	global arr
	if i == 3:
		return arr.append(x)
	elif i < 3:
		return f(x * 2, i + 1), f(x * 3, i + 1)

f(2)
print(len(set(arr)))


# Ответ: 4