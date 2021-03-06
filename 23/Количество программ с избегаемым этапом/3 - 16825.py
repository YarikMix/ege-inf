"""
Сколько существует программ, которые преобразуют исходное число 3 в число 16, и 
при этом траектория вычислений не содержит чисел 6 и 12?
+1
*2
+3
"""

def f(x, y):
	if x < y and x not in (6, 12):
		return f(x + 1, y) + f(x * 2, y) + f(x + 3, y)
	elif x == y:
		return 1
	else :
		return 0

print(f(3, 16))


# Ответ: 22