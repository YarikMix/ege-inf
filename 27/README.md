# Задание 27. Обработка последовательностей

Есть два ~~стула~~ алгоритма решения 27 задачи

## 1 алгоритм

В лоб перебрать все пары чисел<br>

Сделать это можно с помощью двух циклов
```bash
for i in range(0, n - 1):
    for j in range(i + 1, n):
        ...
```

Или с помощью метода combinations из itertools
```bash
from itertools import combinations
for pair in combinations(arr):
	...
```

Этот алгоритм работает за O(n²)<br>
✅Получиться решить пункт a)<br>
❌На пункт б) не хватит памяти

## 2 алгоритм - взять хитросью

Для любой 27 задачи можно придумать решение, работающее за O(1)<br>