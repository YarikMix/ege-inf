def f():
	i = 1
	for a1 in ("А", "О", "У"):
		for a2 in ("А", "О", "У"):
			for a3 in ("А", "О", "У"):
				for a4 in ("А", "О", "У"):
					for a5 in ("А", "О", "У"):
						s = a1 + a2 + a3 + a4 + a5
						if i == 210:
							return s
						i += 1

print(f())  # УОУАУ