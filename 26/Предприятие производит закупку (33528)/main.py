import operator


with open("input.txt") as f:
	N, M = map(int, f.readline().split())
	arr = []
	for _ in range(N):
		s = f.readline().split(" ")
		arr.append({
			"price": int(s[0]),
			"count": int(s[1]),
			"type": s[2]
		})

	# Все продукты типа A
	products_A = list(filter(lambda x: x["type"] == "A", arr))
	# Все продукты типа B
	products_B = list(filter(lambda x: x["type"] == "B", arr))

	# Суммарная цена всех продуктов типа A
	price_A = sum([product["price"] * product["count"] for product in products_A])
	# Суммарная цена всех продуктов типа B
	price_B = sum([product["price"] * product["count"] for product in products_B])

	# print(price_A)  # 2870309
	# print(M - price_A)  # 1129691
	# print(price_B)  # 2574854

	# Сортируем продукты типа B по возрастанию цены
	products_B.sort(key=operator.itemgetter("price"))

	# Покупаем все продукты типа A
	M -= price_A

	count = 0
	# Покупаем столько продуктов типа B, сколько сможем
	for product in products_B:
		if M - product["price"] * product["count"] > 0:
			M -= product["price"] * product["count"]
			count += product["count"]
		else:
			for i in range(product["count"]):
				if M - product["price"] > 0:
					M -= product["price"]
					count += 1
				else:
					break

	print(count)  # Количество купленных продуктов типа B
	print(M)  # Оставшееся сумма денег


# Ответ: 5895 227