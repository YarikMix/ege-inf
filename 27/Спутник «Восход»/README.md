## Спутник «Восход»

На спутнике «Восход» установлен прибор, предназначенный для измерения солнечной активности. В течение времени эксперимента (это время известно заранее) прибор каждую минуту передаёт в обсерваторию по каналу связи положительное целое число, не превышающее 1000, — количество энергии солнечного излучения, полученной за последнюю минуту, измеренное в условных единицах.

После окончания эксперимента передаётся контрольное значение — наибольшее число R, удовлетворяющее следующим условиям:

1) R — произведение двух чисел, переданных в разные минуты;

2) R делится на 26.

Необходимо найти такое число R. Предполагается, что удовлетворяющее условиям контрольное значение существовало в момент передачи. В результате помех при передаче как сами числа, так и контрольное значение могут быть искажены.

Если удовлетворяющее условию контрольное значение определить невозможно, то выводится число 0.

На вход программе в первой строке подаётся количество чисел 1 < N ≤ 100 000. В каждой из последующих N строк записано одно положительное целое число, не превышающее 1000.

Входные данные.

Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество чисел N (1 ≤ N ≤ 100000). В каждой из последующих N строк записано одно натуральное число, не превышающее 1000.

Пример организации исходных данных во входном файле:

5
52
12
39
55
23

Пример выходных данных для приведённого выше примера входных данных:

2860

В ответе укажите два числа: сначала значение искомой суммы для файла А, затем для файла B.

[Задача на сайте Решу ЕГЭ](https://inf-ege.sdamgia.ru/problem?id=27988)

## Решение

**Ответ: 783900 988000**