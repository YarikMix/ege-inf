from itertools import permutations


i = 1
for s in permutations("АОУ"):
	if i == 210:
		print(s)
	i += 1


# Ответ: УОУАУ