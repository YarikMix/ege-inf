"""
Сколько существует программ, для которых при исходном числе 2 результатом является число 28 и 
при этом траектория вычислений содержит число 14?
+1
*2
*3
"""

def f(x, y):
	if x < y:
		return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)
	elif x == y:
		return 1
	else:
		return 0

print(f(2, 14) * f(14, 28))


# Ответ: 38