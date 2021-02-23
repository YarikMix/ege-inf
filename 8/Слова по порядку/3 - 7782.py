def f():
	i = 1
	for a1 in ("Н", "Р", "Т", "У"):
		for a2 in ("Н", "Р", "Т", "У"):
			for a3 in ("Н", "Р", "Т", "У"):
				for a4 in ("Н", "Р", "Т", "У"):
					s = a1 + a2 + a3 + a4
					if i == 215:
						return s
					i += 1

print(f())  # УРРТ