"""
Сколько существует программ, которые преобразуют исходное число 3 в число 20 и 
при этом траектория вычислений содержит число 9 и не содержит числа 15?
+1
+2
"""

def f(x, y):
	if x < y and x != 15:
		return f(x + 1, y) + f(x + 2, y)
	elif x == y:
		return 1
	else:
		return 0

print(f(3, 9) * f(9, 20))


# Ответ: 520