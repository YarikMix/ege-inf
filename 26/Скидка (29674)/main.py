import math

with open("input.txt") as f:
	N = int(f.readline())
	discount = []  # Товары со скидкой <= 50
	products = []  # Остальные товары > 50
	total_sum = 0
	for _ in range(N):
		price = int(f.readline())
		if price > 50:
			products.append(price)
		else:
			total_sum += price

	products.sort()  # Сортируем по возрастанию

	while len(products) > 1:
		total_sum += products[-1]
		discount.append(products[0])
		del(products[0], products[-1])

	total_sum += sum(products) + math.ceil(0.75 * sum(discount))
	print(total_sum, max(discount))

# len(arr) - товаров со скидкой
# len(discount) - товаров со скидкой
# N - len(discount) - товаров без скидки

# total_sum - общая стоимость покупки с учётом скидки
# max(discount) - стоимость самого дорогого товара, на который будет предоставлена скидка

# Ответ: 469784 511