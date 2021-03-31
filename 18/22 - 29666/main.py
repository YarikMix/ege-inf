with open("input.txt") as f:
	arr = [float(s.strip("\n").replace(",", ".")) for s in f.readlines()]

r = []
for i, x in enumerate(arr):
     temp = [x]
     for j in range(i+1, len(arr)):
          if arr[j] < temp[-1]:
               temp.append(arr[j])
          else:
               r.append(sum(temp))
               break
     r.append(sum(temp))
print(int(max(r)))


# Ответ: 358