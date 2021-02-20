with open("input.txt") as f:
	s,n = map(int, f.readline().split())
	mas = [int(f.readline()) for i in range(n)]
	mas.sort()
	newmas = []
	for i in range(len(mas)-1):
		if sum(newmas) + mas[i] <= s:
			newmas.append(mas[i])
		elif sum(newmas) - mas[i-1] + mas[i] <= s:
			del(newmas[-1])
			newmas.append(mas[i])
		else:	
			break
	print(len(newmas), newmas[-1])

# 568 50