from itertools import product


count = 0
for s in product("ЕГЭ", repeat=5):
	if s[0] == "Е" or s[0] == "Э":
		count += 1

print(count)


# Ответ: 162