from itertools import permutations

i = 1
for s in permutations("АОУ"):
	if i == 210:
		print(s)
		break
	i += 1

def f():
	i = 1
	for a1 in "АОУ":
		for a2 in "АОУ":
			for a3 in "АОУ":
				for a4 in "АОУ":
					for a5 in "АОУ":
						s = a1 + a2 + a3 + a4 + a5
						if i == 210:
							return s
						i += 1

print(f())  # УОУАУ