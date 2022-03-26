"""
Тема 3: “Циклы со счетчиком”
	1	Определить, сколько раз последовательность из N произвольных чисел меняет знак (т.е. после положительного
	элемента идет отрицательный и наоборот).
	2	Дан некоторый текст. Определить количество вхождений в него каждого символа.
	3	Вывести на экран следующую последовательность символов:
	* * * * * * *
	  * * * * *
	    * * *
	      *
	    * * *
	  * * * * *
	* * * * * * *
	4	Найти среднее арифметическое делителей числа N.
"""
#1

n = [2, -4, 2.5, -6.5, -7, 2.1, 3, -9]
count = 0

for i in range(0, len(n)-1):
    if (n[i] < 0 and n[i+1] > 0) or (n[i] > 0 and n[i+1] < 0):
        count += 1
print(count)
print("__________________")

#2
s = "Дан некоторый текст. Определить количество вхождений в него каждого символа"
res = {}

for i in s:
    if i in res.keys():
        res[i] += 1
    else:
        res[i] = 1
print(res)
print("__________________")

#3

k = 7
symbol = "*"

for i in range(k, 0, -2):
    s = str(symbol * i)
    space_count = int((k-len(s))/2)
    s = s.rjust(space_count + len(s))
    print(s)
for i in range(3, k+1, 2):
    s = str(symbol * i)
    space_count = int((k - len(s)) / 2)
    s = s.rjust(space_count + len(s))
    print(s)
print("__________________")

#4
N = 28
deliteli = []

for i in range(1, N+1):
    if N % i == 0:
        deliteli.append(i)
print(deliteli)
sr = sum(deliteli) / len(deliteli)
print(round(sr, 2))