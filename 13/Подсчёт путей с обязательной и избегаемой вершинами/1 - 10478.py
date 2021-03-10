def f(letter):
	if letter == "А":
		return 1

	if letter == "Б":
		return sum([f(l) for l in "А"])

	if letter == "В":
		return sum([f(l) for l in "БАГ"])

	if letter == "Г":
		return sum([f(l) for l in "АД"])

	if letter == "Д":
		return sum([f(l) for l in "А"])

	if letter == "Е":
		return sum([f(l) for l in "БВ"])

	if letter == "Ж":
		return sum([f(l) for l in "ЕВЗ"])

	if letter == "З":
		return sum([f(l) for l in "ВГД"])

	if letter == "И":
		return sum([f(l) for l in "Ж"])

	if letter == "Л":
		return sum([f(l) for l in "И"])

	if letter == "М":
		return sum([f(l) for l in "Л"])

print(f("М"))


# Ответ: 16