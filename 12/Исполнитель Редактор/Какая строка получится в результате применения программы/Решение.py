s = "8" * 68

while s.count("222") or s.count("888"):
	if s.count("222"):
		s = s.replace("222", "8", 1)
	else:
		s = s.replace("888", "2", 1)

print(s)


# Ответ: 28