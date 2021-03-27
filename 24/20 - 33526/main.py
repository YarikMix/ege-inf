import string


def get_key_by_value(val, d):
	for key, value in d.items():
		if value == val:
			return key

with open("input.txt") as f:
	s = f.readline()

d = {s: 0 for s in string.ascii_uppercase}

for i in range(1, len(s) - 1):
	if s[i - 1] == s[i + 1]:
		d[s[i]] += 1

max_count = max(d.values())
character = get_key_by_value(max_count, d)

print(character)


# Ответ: D