with open("input.txt") as f:
	s = f.readline()

cur_len = 1
max_len = 1
for i in range(len(s) - 1):
	if s[i] != s[i + 1]:
		cur_len += 1
	else:
		max_len = max(max_len, cur_len)
		cur_len = 1

print(max_len)


# Ответ: 42