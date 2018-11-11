
__author__ = 'Сотников Владимир А.'
print("Данный файл содержит решения ДЗ №3 для блока Normal, автор", __author__)


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
	fiba=[1,1]
	j=2
	
	idx_init=0	#меточка для фильтраот n до m

	while j<=m:
		new_memb=fiba[j-2]+fiba[j-1]
		fiba.append(new_memb)
		if new_memb<n:
			idx_init=j
		j+=1

	idx_init+=1
	Arr_what_I_want=fiba[idx_init:]
	print(Arr_what_I_want)

	return bool(1)			#типа отработал до конца


#========================================================================================================

print("="*15 + " "*5+ "Задача 1")
print("Для ряда Фибоначчи введите: ")
n=int(input("c какого числа (n) строить последовательность = "))
m=int(input("до какого числа (m) строить последовательность = "))

if (n>=m):
	n,m=m,n

if m!=0:
	fibonacci(n,m)


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


"""
	Попробуем вмето пузырька, пропорционального (N*N), решить за N/2. Для этого:
	1. На первом шаге рассмотрим всю последовательность и на ее края поставим мин и макс значения
	2. На втором шаге последовательность из генеральной, начиная с индекса 1 до ((len)-2). Так же мин и макс поместим на края выборки
	3. и т.д. с шагом (+1) слева и (-1) справа будем стягиваться к центру

	Хотя, неизвестно быстрее ли работает такой алгоритм, так как поиск min и max внутри Python может быть пузырьком :)
"""

def sort_to_max(origin_list):
	
	Sorted_list=[]
	Sorted_list=origin_list
	steps_count=len(Sorted_list)//2		
	j=0

	while j<steps_count:
		RightBound=(len(Sorted_list)-1-j)
		tmp_arr=[]
		tmp_arr=Sorted_list[j:RightBound+1]
		
		Mi=min(tmp_arr)
		Ma=max(tmp_arr)

		if Sorted_list[j]>Mi:
			idx_Mi=Sorted_list.index(Mi,j,RightBound+1)
			Sorted_list[j],Sorted_list[idx_Mi]=Sorted_list[idx_Mi],Sorted_list[j]
		
		if Sorted_list[RightBound]<Ma:
			idx_Ma=Sorted_list.index(Ma,j,RightBound+1)		
			Sorted_list[RightBound],Sorted_list[idx_Ma]=Sorted_list[idx_Ma],Sorted_list[RightBound]

		j+=1	

	print(Sorted_list)
	return Sorted_list

print("="*15 + " "*5+ "Задача 2")
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

#========================================================================================================


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print("="*15 + " "*5+ "Задача 3  (возможно, не совсем понял условие)")

def My_filter(WhereFind,WhatFind,StrongCondit):
	Filtered_arr=[]

	for elem in WhatFind:
		for ell in WhereFind:
			if StrongCondit:
				if elem==ell: 
					Filtered_arr.append(ell)
			else:
				if ell.find(elem)!=-1: 
					Filtered_arr.append(ell)

	return Filtered_arr



Init_mass=["Алыча","Ананас","Аннона пурпурная","Аннона разнолистная","Аннона сетчатая","Антильский абрикос","Апельсин","Араза","Лайм","Лангсат","Лардизабала","Лимон","Лимон дикий","Личи","Лукума","Лума остроконечная"]
i=0
for elem in Init_mass:
	Init_mass[i]=elem.lower()
	i+=1

Mass_for_find=["лимон", "аннона"]

Filtered_arr=[]
Filtered_arr=My_filter(Init_mass,Mass_for_find,True)
print("При требовании строгого соответствия: ")
print(Filtered_arr)

Filtered_arr=[]
Filtered_arr=My_filter(Init_mass,Mass_for_find,False)
print("При требовании как бы Like: ")
print(Filtered_arr)

#========================================================================================================
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

"""
Логика:
	1. Через две точки всегда можно провести прямую, причем только одну
	2. Раз прямая, то описывается ф-ей вида y=kx+b, где b - сдвиг, а k- определяет tg угла наклона 
		// tg - отлично, но это sin/cos, а значит плохо при угле 90, что соотв прямой || оси ординат ( !!! надо проверять на деление на 0)
	3. При равенстве k у двух прямых, надо полагать они параллельны
	4. Если известны координыты (X,Y) точек, то нахождение k и b - это решение системы из 2х ур-ий с 2мя неизвестными
	5. Задача проверки имменно параллелограмма, а не трапеции, например, подсказывает, что достаточно проверить только любые две прямые на || 
	6. п.5 еще стоит дополнить проверкой, чтобы не было повторных точек, ибо тогда точка по факту одна, 
		а через неё можно провести бесконечное множество прямых = фиаско...
"""


Coord_array=[]				# Массив точек сделаем глобальным, чтоб отработать знания с урока :)


def Str_to_list(user_str):
	my_l=[]
	a=user_str.index(";")	
	my_l.append(float(user_str[0:a]))
	my_l.append(float(user_str[a+1:]))
	return my_l


#Сортировка заданных точек методом пузырька сначала по X, потом по Y координатам (по Y только в случае равенства X)
def Sort_Points():
	
	cnt=len(Coord_array)-1
	WasZamena=True			#True означает, что на очередном пробеге был изменен порядок эл-тов. При False - выход из while

	while WasZamena==True:
		WasZamena=False
		j=1
		while j<=cnt:
			if Coord_array[j][0]<Coord_array[j-1][0]:
				WasZamena=True
				Coord_array[j],Coord_array[j-1]=Coord_array[j-1],Coord_array[j]
			j+=1

	WasZamena=True
	while WasZamena==True:
		WasZamena=False
		j=1
		while j<=cnt:
			if Coord_array[j][0]==Coord_array[j-1][0] and Coord_array[j][1]<Coord_array[j-1][1]:
				WasZamena=True
				Coord_array[j],Coord_array[j-1]=Coord_array[j-1],Coord_array[j]
			j+=1
	
	#здесь же проверка на совпадающие точки (вдруг ошиблись при вводе)
	NOTtrouble=True
	j=1
	while j<=cnt:
		if Coord_array[j][0]==Coord_array[j-1][0] and Coord_array[j][1]==Coord_array[j-1][1]:
			trouble=True
		j+=1

	return NOTtrouble



#Вычисляет коэффициенты k и b для прямой 
def Guess_coeff_for_line(tckA,tckB):
	if (tckB[0]-tckA[0])!=0:
		k=(tckB[1]-tckA[1])/(tckB[0]-tckA[0])
		b=tckA[1]-k*tckA[0]
	else:
		k=0
		b=tckA[1]
	return k


def CheckParallelogramm():
	k1=Guess_coeff_for_line(Coord_array[0],Coord_array[1])
	k2=Guess_coeff_for_line(Coord_array[2],Coord_array[3])

	if k1==k2:
		#надо проверять на || другие два отрезка
		k3=Guess_coeff_for_line(Coord_array[1],Coord_array[3])
		k4=Guess_coeff_for_line(Coord_array[0],Coord_array[2])

		if k3==k4:
			return bool(1)
		else:
			return bool(0)
	else:
		return bool(0)



print("="*15 + " "*5+ "Задача 4")
print("Введите через тчк с зпт (;) координаты X и Y для точек: ")

A1=input("первой ")
A2=input("второй ")
A3=input("третьей ")
A4=input("четвертой ")

Coord_array.append(Str_to_list(A1))
Coord_array.append(Str_to_list(A2))
Coord_array.append(Str_to_list(A3))
Coord_array.append(Str_to_list(A4))

res=False

if Sort_Points():
	res=CheckParallelogramm()
	print("Заданные точки с сортировкой: ")
	print(Coord_array)

print("Параллелограмм = " + str(res))


