"""
Тема 5: “Условие else в циклах”
	1	Дана последовательность чисел. Проверить, есть ли в ней хотя бы одно число с делителями 2, 5 и 7.
	Если да, вывести его на экран. Если нет, вывести соответствующее сообщение.
	2	Дана последовательность чисел. Проверить, являются ли все элементы последовательности нечетными числами.
	3	Дан список продуктов с ценами на них: ‘milk’ - $12, ‘bread’ - $10, ‘meat’ - $60, ‘vegetable mix’ - $20, ‘
	fruit mix’ - $35, ‘fish’ - $45, ‘eggs’ - $15, ‘cake’ - $15. У Марты есть $100.
	Какое максимальное количество продуктов она может купить? Выведите на экран список этих продуктов.
	В случае если Марта сможет купить все продукты из списка, выведите соответствующее сообщение.
	Решите эту же задачу для Алекса, у которого есть $250.
"""
#1

numb = [13, 11, 1, 17, 9, 19, 19, 19]

for i in numb:
    if i % 2 == 0:
        print(i, "Делится на 2")
        break
    elif i % 5 == 0:
        print(i, "Делится на 5")
        break
    elif i % 7 == 0:
        print(i, "Делится на 7")
        break
else:
    print("Не делится")
print("________________")

#2
numb = [13, 11, 1, 17, 9, 19, 19, 10]

for i in numb:
    if i % 2 == 0:
        print("Четные числа присутствуют")
        break
else:
    print("Все элементы не четные")
print("_________________")

#3

goods = {"milk": 12, "bread": 10, "meat": 60, "vegetable mix": 20, "fruit mix": 35, "fish": 45, "eggs": 15, "cake": 15}
goods_sort = {"bread": 10, "milk": 12, "eggs": 15, "cake": 15, "vegetable mix": 20, "fruit mix": 35, "fish": 45, "meat": 60}

amount = 250
count = 0

for names, price in goods_sort.items():
    amount = amount - price
    if amount < 0:
        print(count)
        break
    print(names, end=" ")
    count += 1
else:
    print("\nВсе товары были куплены")
