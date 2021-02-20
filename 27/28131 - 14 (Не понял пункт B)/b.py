# Решение №1
with open("inputB.txt") as f:
	m = 120
	# создание массива для максимальных значений
	# для каждого из остатков
	r = [0] * m
	# обнуление переменных для записи ответа
	left = 0
	right = 0
	# ввод количества элементов
	n = int(f.readline())
	# ввод значений, поиск искомой пары
	for i in range(n):
	    a = int(f.readline())
	    p = a % m;
	    if r[(m - p) % m] > a and r[(m - p) % m] + a > left + right:
	        #обновление ответа
	        left = r[(m - p) % m]
	        right = a;
	    # обновление элемента r для соответствующего остатка
	    if a > r[p]:
	        r[p] = a
	print(left, right)

# Решение №2
with open("inputB.txt") as f:
	N = int(f.readline()) # Ввожу N (самая сложная чать програмы)

	delimer = 120 # В данном случае делимость на 120
	pair = 0,0 # Делаем лист из 2 элементов
	rems = { i:0 for i in range(delimer) } # Заполняем и обнуляем массив с остатками от деления

	for i in range(N): # Начинаем принимать числа
	    x = int(f.readline()) # Взял число
	    x_pair = (delimer-x%delimer)%delimer # Нашел до него недостающий кусок, например x = 100, нашел 20, 120 кратно
	    if rems[x_pair] and rems[x_pair]+x> pair[0] + pair[1] and rems[x_pair]>x: # Если сумма больше, и "предыдущий"
	                                                                            # элемент пары больше
	        pair = rems[x_pair],x # делаю лист из этих двух элементов
	        
	    rems[x%delimer] = max(rems[x%delimer],x) # т.к. найти максимальную, то пишу max("предыдущий" эл., этот элемент)
	print(*pair) # Привожу к виду [140, 100] -> 140 100

# A 8096 6544
# b 9993 9927