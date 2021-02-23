# Решение для B
with open("inputB.txt") as f:
	arr = [int(i) for i in f.readlines()][1:]

	# М1 — самое большое число, дающее при делении на 3 остаток 1,
	# M2 — самое большое число, дающее при делении на 3 остаток 2,
	# M3_first — самое большое число, кратное 3,
	# M3_second — второе по величине число, кратное 3
	M1 = max(filter(lambda x: x % 3 == 1, arr), default=0)
	M2 = max(filter(lambda x: x % 3 == 2, arr), default=0)
	M3_first = max(filter(lambda x: x % 3 == 0, arr), default=0)
	M3_second = max(filter(lambda x: x % 3 == 0 and x != M3_first, arr), default=0)

	res = max(M1 + M2, M3_first + M3_second)
	print(res)

# A 19020
# B 19998