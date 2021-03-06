"""
Сколько существует программ, которые преобразуют исходное число 2 в число 14, и 
при этом траектория вычислений не содержит чисел 5 и 10?
+1
*2
+3
"""

def f(x, y):
	if x < y and x not in (5, 10):
		return f(x + 1, y) + f(x * 2, y) + f(x + 3, y)
	elif x == y:
		return 1
	else:
		return 0

print(f(2, 14))


# Ответ: 26