def M(n):
    arr = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            arr.extend([d, n // d])
        d += 1
    arr.sort()
    try:
    	return arr[0] + arr[-1]
    except:
    	return 0

k = 0
for n in range(452022, 100000000000):
	if M(n) % 7 == 3:
		print(n, M(n))
		k += 1
		if k == 5:
			break


"""
Ответ:
452025 150678
452029 23810
452034 226019
452048 226026
452062 226033
"""