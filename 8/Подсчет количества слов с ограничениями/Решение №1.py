count = 0
for s1 in "ЕГЭ":
	for s2 in "ЕГЭ":
		for s3 in "ЕГЭ":
			for s4 in "ЕГЭ":
				for s5 in "ЕГЭ":
					s = s1 + s2 + s3 + s4 + s5
					if s[0] == "Е" or s[0] == "Э":
						count += 1

print(count)


# Ответ: 162