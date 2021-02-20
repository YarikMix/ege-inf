# Решение №1
with open("input.txt") as f:
	prevsymbol = ''
	max_len = 0  # Максимальное количество
	cur_len = 0  # Текущий счетчик
	for symbol in f.read():
		if symbol != prevsymbol:
			max_len = max(max_len, cur_len)
		else:
			cur_len = 1  # Сбрасываем счётчик
		cur_len += 1
		prevsymbol = symbol
	print(max_len)  # 35

# Решение №2
with open("input.txt") as f:
	s = f.read()
	max_len = 0  # Максимальное количество
	cur_len = 0  # Текущий счетчик
	for i in range(len(s)-1):
		if s[i] != s[i+1]:
			max_len = max(max_len, cur_len)
		else:
			cur_len = 1 # Сбрасываем счётчик
		cur_len += 1
	print(max_len)  # 35