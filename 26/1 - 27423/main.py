with open("input.txt") as f:
	s, n = map(int, f.readline().split())
	arr = [int(f.readline()) for i in range(n)]
	arr.sort()
	res = []
	for i in range(len(arr)-1):
		if sum(res) + arr[i] <= s:
			res.append(arr[i])
		elif sum(res) - arr[i-1] + arr[i] <= s:
			del(res[-1])
			res.append(arr[i])
		else:	
			break
	print(len(res), res[-1])  # 568 50

