s = "МЕТРО"
count = 0
for s1 in s:
	for s2 in s:
		for s3 in s:
			for s4 in s:
				r = s1 + s2 + s3 + s4
				if r[0] in ("М", "Т", "Р") and r[-1] in ("Е", "О"):
					count += 1 
print(count)  # 150