def f():
	i = 1
	for a1 in ("Л", "Н", "Р", "Т"):
		for a2 in ("Л", "Н", "Р", "Т"):
			for a3 in ("Л", "Н", "Р", "Т"):
				for a4 in ("Л", "Н", "Р", "Т"):
					for a5 in ("Л", "Н", "Р", "Т"):
						s = a1 + a2 + a3 + a4 + a5
						if i == 150:
							return s
						i += 1

print(f())  # ЛРННН