with open("input.txt") as f:
	s = f.readline()
	max_len = 0
	cur_len = 0
	for i in range(len(s)-1):
		if s[i] == s[i+1] == "X":
			cur_len += 1
		else:
			max_len = max(max_len, cur_len)
			cur_len = 0
	print(max_len + 1) 

# Ответ: 19

import itertools

list_cycle = itertools.cycle(s)
next(s)

with open("input.txt") as f:
	s = f.readline()

for i in range(len(s)):
	current_elem = 
	next_elem = next(list_cycle)
