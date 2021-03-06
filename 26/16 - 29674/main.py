with open("input.txt") as f:
	N = int(f.readline())
	arr = [int(f.readline()) for _ in range(N)]

exclude = sorted(filter(lambda x: x <= 50, arr))
arr = sorted(filter(lambda x: x > 50, arr))
total_sum = sum(exclude)
discount = []

while len(arr) > 1:
	total_sum += arr[-1]
	discount.append(arr[0])
	del(arr[0], arr[-1])

total_sum += sum(discount) * 0.75
total_sum += sum(arr)
total_sum = round(total_sum)

print(total_sum, max(discount))

# print(f"Со скидкой {len(discount)}")
# print(f"Без скидки {N - len(exclude) - len(discount)}")


# Ответ: 469784 511