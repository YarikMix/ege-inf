"""
Сколько существует программ, которые преобразуют исходное число 1 в число 25, и 
при этом траектория вычислений не содержит число 24?
+1
сделай нечётное
"""

def f(x, y):
	if x < y and x != 24:
		return f(x + 1, y) + f(2 * x + 1, y)
	elif x == y:
		return 1
	else :
		return 0

print(f(1, 25))


# Ответ: 10