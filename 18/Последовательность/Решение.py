with open("input.txt") as f:
	arr = [float(s.replace(",", ".")) for s in f.readlines()]

max_sum = 0
for i, x in enumerate(arr):
     temp = [x]
     for j in range(i + 1, len(arr)):
          if arr[j] < temp[-1]:
               temp.append(arr[j])
          else:
               max_sum = max(max_sum, sum(temp))
               break
print(int(max_sum))


# Ответ: 358