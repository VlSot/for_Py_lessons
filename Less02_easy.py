
import random

__author__ = 'Сотников Владимир А.'
print("Данный файл содержит решения ДЗ №2 для блока Easy, автор", __author__)

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
print("="*15 + " "*5+ "Задача 1")
MyFru=["яблоко", "банан", "киви", "арбуз"]

j=1
for fr in MyFru:
	MyStr=str(j) +'.' +  '{:>10}'.format(fr)#.format(<)
	print(MyStr) 
	j+=1


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print("="*15 + " "*5+ "Задача 2")
print("Переходим ко второй задаче easy. Два списка заполним случайно значениями int от А до Б")

a=int(input("Введите нижний предел для random.randint (а) = " ))
b=int(input("Введите верхний предел для random.randint (b) = " ))


n=int(input("Введите количество элементов в первом списке: "))
j=0

list_01=[]
list_02=[]

while j<=(n-1):
	list_01.append(random.randint(a, b))
	j+=1

n=int(input("Введите количество элементов во втором списке: "))
j=0
while j<=(n-1):
	list_02.append(random.randint(a,b))
	j+=1


print("Сгенерировал списки:")
print(list_01)
print(list_02)

for elem in list_02:
	while (elem in list_01):
		list_01.remove(elem)

print("Измененный первый без элементов второго:")
print(list_01)



# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print("="*15 + " "*5+ "Задача 3")
print("Переходим к третьей задаче easy. Дабы не напрягать пользователя, список заполним случайными значениями int от А до Б")
a=int(input("Введите нижний предел для random.randint (а) = " ))
b=int(input("Введите верхний предел для random.randint (b) = " ))


n=int(input("Введите количество элементов в списке: "))
j=0

list_01=[]
list_02=[]

while j<=(n-1):
	list_01.append(random.randint(a, b))
	j+=1

for elem in list_01:
	if (elem%2)>0:
		list_02.append(elem*2)
	else:
		list_02.append(elem/4)

print("Исходная последовательность:")
print(list_01)
print("Измененная: ")
print(list_02)


print(" ")
print("="*10 +" "*3+ "отработал на easy"+" "*3+"="*10)