def f(s):
	while s.count("01") or s.count("02") or s.count("03"):
		s = s.replace("01", "2302", 1)
		s = s.replace("02", "10", 1)
		s = s.replace("03", "201", 1)
	return s

for x in range(50):
	for y in range(50):
		for z in range(50):
			s = "0" + "1" * x + "2" * y + "3" * z
			if f(s).count("1") == 40 and f(s).count("2") == 10 and f(s).count("3") == 8:
				print(s.count("1"))
				exit()


# Ответ: 6