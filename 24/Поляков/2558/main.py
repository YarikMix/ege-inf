with open("input.txt") as f:
	n = 0
	for s in f.readlines():
	    flag = 0
	    for i in range(len(s) - 2):
	        if s[i]=="A" and s[i+2] == "R":
	            flag = True
	            if True:
	                n += 1
	                break
	print(n)


# Ответ: 784