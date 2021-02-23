s = "СЛОН"
count = 0
for s1 in s:
	for s2 in s:
		for s3 in s:
			for s4 in s:
				for s5 in s:
					r = s1 + s2 + s3 + s4 + s5
					if r.count("С") == 1:
						count += 1 
print(count)  # 405