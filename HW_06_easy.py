
from math import sqrt

__author__ = 'Сотников Владимир А.'
print("Данный файл содержит решения ДЗ №6 для блока easy, автор", __author__)



class Triang:

	def __init__(self,Mass_coord):
		self.Mass_coord=Mass_coord
				


	def CalcSquare(self):
		# формула Герона: площадь пропорциональна корню из произведения разностей полупериметра 
		# треугольника (p) и каждой из его сторон (a, b, c)		
		poluper=self.CalcPerim()/2
		MassLength=self.FillMassLehgth()
		Squar=1
		
		for elem in MassLength:
			Squar=Squar*(poluper-elem)

		Squar=sqrt(Squar*poluper)
		return round(Squar,2)


	def CalcDepth(self):
		# Площадь высчитали по трем сторонам - самый легкий способ для алгоритмизации. 
		# Но есть формула для площади S= 1/2 *a*h, откуда можно вычислить h, спущенную на а. 
		# Т.е. для нас h=2S/a
		S=self.CalcSquare()
		Our_Stor=self.FillMassLehgth()

		h=[]
		h=[round(2*S/elem,2) for elem in Our_Stor]

		return h


	def CalcPerim(self):
		MassLength=[]
		MassLength=self.FillMassLehgth()
		Perim=0
		
		for elem in MassLength:
			Perim=Perim+elem

		return round(Perim,2)


	def FillMassLehgth(self):

		dl_01=sqrt((self.Mass_coord[0][0]-self.Mass_coord[1][0])**2+(self.Mass_coord[0][1]-self.Mass_coord[1][1])**2)
		dl_02=sqrt((self.Mass_coord[0][0]-self.Mass_coord[2][0])**2+(self.Mass_coord[0][1]-self.Mass_coord[2][1])**2)
		dl_03=sqrt((self.Mass_coord[2][0]-self.Mass_coord[1][0])**2+(self.Mass_coord[2][1]-self.Mass_coord[1][1])**2)

		Otrezki=[]
		Otrezki.append(dl_01)
		Otrezki.append(dl_02)
		Otrezki.append(dl_03)

		return Otrezki



# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

print("")
print("="*15 + " "*5+ "Задача 1. Треугольник")

def Str_to_list(user_str):
	my_l=[]
	a=user_str.index(";")	
	my_l.append(float(user_str[0:a]))
	my_l.append(float(user_str[a+1:]))
	return my_l


Coord_array=[]

Q=input("Хотите ввести свои точки для треуголинка? y/n ")

if Q=="y":
	print("Введите через тчк с зпт (;) координаты X и Y для точек: ")
	A1=input("первой ")
	A2=input("второй ")
	A3=input("третьей ")
	Coord_array.append(Str_to_list(A1))
	Coord_array.append(Str_to_list(A2))
	Coord_array.append(Str_to_list(A3))
else:
	Coord_array.append([-1,1])
	Coord_array.append([-3,3])
	Coord_array.append([-3,1])


User_triang=Triang(Coord_array)
print("Площадь треугольника, построенного на точках ",Coord_array, ", равна ", str(User_triang.CalcSquare())," ; периметр ", str(User_triang.CalcPerim()),"; высоты: " , str(User_triang. CalcDepth()) )







# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


"""
	1. В этом задании точек уже 4, а значит способ их попарного соединения НЕОДНОЗНАЧЕН - необходимо сортировать на плоскости
	2. Из п.1, т.е. после упорядочения, противоположные стороны проверим на || , а вторые на равенство. Если и то и то true, то у нас равнобедренная трапеция
	3. С длинами проще всего работать, а значит площадь трапеции определим через четыре стороны (формула посложнее, но геометрический вывод же не требуется?!)
	4. С длинами проще всего работать - отсюда и периметр легко находится	 
"""


class Trapeciya:
	def __init__(self,Mass_coord):
		self.Mass_coord=Mass_coord


	def Length_Otrezok(self,tckA,tckB):
		return sqrt((tckA[0]-tckB[0])**2+(tckA[1]-tckB[1])**2)



	def FillMassLehgth(self):
		
		Otrezki=[]
		Otrezki.append(self.Length_Otrezok(self.Mass_coord[0],self.Mass_coord[1]))
		Otrezki.append(self.Length_Otrezok(self.Mass_coord[1],self.Mass_coord[2]))
		Otrezki.append(self.Length_Otrezok(self.Mass_coord[2],self.Mass_coord[3]))		
		Otrezki.append(self.Length_Otrezok(self.Mass_coord[0],self.Mass_coord[2]))

		return Otrezki



	def CalcPerimTrap(self):
		
		Stor=self.FillMassLehgth()
		Perim=0
		
		for elem in Stor:
			Perim=Perim+elem

		print("Стороны ", Stor)
		return round(Perim,2)




	def CalcSquareTrap(self):
		# https://100formul.ru/48/
		Data_forTrap=self.CheckRavnTrapeciya()
		Squar=-1

		if Data_forTrap[0]==False:
			return Squar

		if Data_forTrap[2]==1:
			osn01=self.Length_Otrezok(self.Mass_coord[0],self.Mass_coord[1])
			osn02=self.Length_Otrezok(self.Mass_coord[2],self.Mass_coord[3])
		elif Data_forTrap[2]==2:
			osn01=self.Length_Otrezok(self.Mass_coord[1],self.Mass_coord[2])
			osn02=self.Length_Otrezok(self.Mass_coord[0],self.Mass_coord[3])
		else:
			return Squar

		a=min(osn01,osn02)
		b=max(osn01,osn02)
		c=Data_forTrap[3][0]		
		d=Data_forTrap[3][1]

		# Неприятная формула, зато не зависим от углов и можно считать неравнобокие 
		# трапеции... в перспективе при коммерциализации этого кода :)
		Squar=(a+b)/2*sqrt(c**2-(((b-a)**2+c**2-d**2)/(2*(b-a)))**2)		#http://tutata.ru/185
		return round(Squar,2)


	
	def Guess_coeff_for_line(self,tckA,tckB):
		if (tckB[0]-tckA[0])!=0:
			k=(tckB[1]-tckA[1])/(tckB[0]-tckA[0])
			b=tckA[1]-k*tckA[0]
		else:
			k=0
			b=tckA[1]
		return k


	def CheckRavnTrapeciya(self):
		# После упорядочения точек остается проверить попарно прямые 01 и 23 ; 12 и 03
		All_for_Trap=[False,False,-1,[-1,-1]]
		Ravnobedr=False

		k1=self.Guess_coeff_for_line(self.Mass_coord[0],self.Mass_coord[1])
		k2=self.Guess_coeff_for_line(self.Mass_coord[2],self.Mass_coord[3])

		dl_01=-1
		dl_02=-2


		if k1==k2:		#Проверка на паралельность двух сторон: это подтвердит с трапецией ли работаем, а так же определит длины двух непараллельных сторон
			
			#надо проверять на равенство длин другие 2 отрезка
			dl_01=self.Length_Otrezok(self.Mass_coord[1],self.Mass_coord[2])
			dl_02=self.Length_Otrezok(self.Mass_coord[0],self.Mass_coord[3])
			
			if dl_01==dl_02:
				Ravnobedr=True

			All_for_Trap=[True,Ravnobedr,1,[dl_01,dl_02]]			# Трапеция , Равнобедренность , 1 пара точек для || линий,  длина непараллельных стороны

		else:			
			k3=self.Guess_coeff_for_line(self.Mass_coord[1],self.Mass_coord[2])
			k4=self.Guess_coeff_for_line(self.Mass_coord[0],self.Mass_coord[3])
			
			if k3==k4:
			
				dl_01=self.Length_Otrezok(self.Mass_coord[0],self.Mass_coord[1])
				dl_02=self.Length_Otrezok(self.Mass_coord[2],self.Mass_coord[3])
				
				if dl_01==dl_02:
					Ravnobedr=True

				All_for_Trap=[True,Ravnobedr,2,[dl_01,dl_02]]		# Равнобедренность , 2 пара точек для || линий  ,  длина равнобокой стороны

		return All_for_Trap



# точек уже 4, а значит способ их попарного соединения НЕОДНОЗНАЧЕН - необходимо сортировать на плоскости
# сделаем это разово, для этого целесообразнее не включать функцию в класс, а оставить отдельно
# ниже проводится пузырьком сначала по X, потом по Y (только в случае равенства X)
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



print("")
print("="*15 + " "*5+ "Задача 2. Трапеция")

Coord_array=[]
Q=input("Хотите ввести свои точки для трапеции? y/n ")

if Q=="y":
	print("Введите через тчк с зпт (;) координаты X и Y для точек: ")
	A1=input("первой ")
	A2=input("второй ")
	A3=input("третьей ")
	A4=input("четвертой ")
	
	Coord_array.append(Str_to_list(A1))
	Coord_array.append(Str_to_list(A2))
	Coord_array.append(Str_to_list(A3))	
	Coord_array.append(Str_to_list(A4))

else:
	Coord_array.append([1,1])
	Coord_array.append([2,4])
	Coord_array.append([5,1])
	Coord_array.append([4,4])



if Sort_Points():
	User_trap=Trapeciya(Coord_array)
	Params_trap=User_trap.CheckRavnTrapeciya()
	print("Четырехугольник, построенный на точках ",Coord_array, ", \nявляется трапецией - ", str(Params_trap[0]),"; \nравнобокой - ",str(Params_trap[1]),"; \nпериметр ",str(User_trap.CalcPerimTrap())," ; площадь ", str(User_trap.CalcSquareTrap()))
else:
	print("Трудности при сортировке точек. Видимо, введенные координаты не образуют трапецию")