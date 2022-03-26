"""
Тема 1: “Ветвления”
	1	Дана точка M с координатами (x, y). Определить месторасположение этой точки в декартовой системе координат:
	    •	является началом координат
	    •	лежит на одной из координатных осей
	    •	расположена в одном из координатных углов
	2	Выяснить, пересекаются ли параболы y = ax2 + bx + c и y = dx2 + ex + f. Если да, найти точки пересечения.
	3	Дан массив целых чисел. Найти его минимальный и максимальный элементы. Если минимальный элемент расположен
	раньше максимального, найти среднее арифметическое всех элементов между ними, а если после - заменить данные элементы
	на их среднее геометрическое.
"""

#1
m = (2, 5)

if m[0] == 0 and m[1] == 0:
    print("Точка лежит в начале координат")
elif m[0] == 0:
    print("Точка лежит на оси Х")
elif m[1] == 0:
    print("Точка лежит на оси Y")
else:
    print("Точка расположена в одном из координатных углов")

#3
m = [2, 77, 6, 1, 4, 6, 76, 7]
m_max = max(m)
m_min = min(m)

index_m_max = m.index(m_max)
index_m_min = m.index(m_min)

if index_m_min < index_m_max:
    sub_m = m[index_m_min+1: index_m_max]
    result = sum(sub_m) / len(sub_m)
    print("Среднее арифметическое:", result)
else:
    sub_m = m[index_m_max+1: index_m_min]
    sr_geom = 1
    for i in sub_m:
        sr_geom *= i
    sr_geom **= 1/len(sub_m)
    m[index_m_max+1: index_m_min] = [sr_geom] * len(sub_m)
    print("Среднее геометрическое:", sr_geom, m)