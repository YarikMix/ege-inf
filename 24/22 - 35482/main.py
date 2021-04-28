from collections import Counter

def func(s):
	"""Возвращает символ, который встречается в строке чаще всего"""
	return Counter(s).most_common()[0][0]

with open("input.txt") as f:
	arr = [s.count("G") for s in f.readlines()]
	min_g = min(arr)  # 18

with open("input.txt") as f:
	for s in f.readlines():
		if s.count("G") == min_g:
			print(func(s))
			break