
from random import randint


__author__ = 'Сотников Владимир А.'
print("Данный файл содержит решения ДЗ №7, автор", __author__)


Bound_l=1
Bound_u=90
SpecChar="—"


def Unic_value(Arr,My_n):		
		
	I = iter(Arr) # Ручной способ итераций: имитация цикла for
	while True:
		try: 
			X = next(I) 		# Или I.__next__
		except StopIteration:
			return True
			break

		if X==My_n:
			return False



def MayBeWin(Arr):
	for elem in Arr:
		if elem!=SpecChar:
			return False

	return True




class LotoCard:


	def __init__(self, NumRyad, NumCifrInRyad, NumPosInRyad,NameCard):		
		self.NumRyad=NumRyad		
		self.NumCifrInRyad=NumCifrInRyad
		self.NumPosInRyad=NumPosInRyad
		self.NameCard=NameCard



	def FillCard(self):			
		All_Use_Num_onCard=[]
		Posit_Num_In_Line=[]
		tmp_r=[]

		i=1
		while i<=self.NumRyad:
			N_ryad=self.GenerateRyad(All_Use_Num_onCard)								
			All_Use_Num_onCard=All_Use_Num_onCard+sorted(N_ryad)			#встроенная функция, использующая протокол итераций
			
			tmp_r=self.Generate_Position_OnCard()
			Posit_Num_In_Line=Posit_Num_In_Line+tmp_r
			i+=1
		
		iitg_mass=[]
		iitg_mass.append(All_Use_Num_onCard)	
		iitg_mass.append(Posit_Num_In_Line)	

		return iitg_mass 											#Loto_Card	



	def GenerateRyad(self,FullCard):
		CifrInRyad=[]		#CifrInRyad =[randint(1,90) for elem in range(self.NumCifrInRyad)]
				
		i=1
		while i<=self.NumCifrInRyad:
			j=randint(Bound_l,Bound_u)

			# __next__
			if Unic_value(FullCard,j)==True and Unic_value(CifrInRyad,j)==True:
				CifrInRyad.append(j)
				i+=1
			
		# print(CifrInRyad)		
		return CifrInRyad



	def Generate_Position_OnCard(self):
		# CifrInRyad =[randint(0,self.NumPosInRyad-1) for elem in range(self.NumCifrInRyad)]
		Mass_pos=[]
		# for i in range(self.NumCifrInRyad):
		# 	r=randint(0,self.NumPosInRyad-1)
		# 	if r not in Mass_pos: Mass_pos.append(r)
		i=1
		while i<=self.NumCifrInRyad:
			j=randint(0,self.NumPosInRyad-1)

			if Unic_value(Mass_pos,j)==True:
				Mass_pos.append(j)
				i+=1

		# print("Массив позиций: ",sorted(Mass_pos))
		return sorted(Mass_pos)



	def Shapka_for_Card(self,Rovn):

		tit=self.NameCard
		n=len(tit)
		rovn_Tit=(Rovn-len(tit)-2)//2

		print("."*rovn_Tit," ",self.NameCard," ","."*rovn_Tit)
		print("-"*Rovn)

		

	def PrintCard(self,arr_loto,arr_pos):
		
		Rovn=3*self.NumPosInRyad
		self.Shapka_for_Card(Rovn)

		i=0
		while i<=self.NumRyad-1:			
			intNum=arr_loto[i*(self.NumCifrInRyad):(i+1)*(self.NumCifrInRyad)]
			posNum=arr_pos[i*(self.NumCifrInRyad):(i+1)*(self.NumCifrInRyad)]
	
			print(self.Prepare_Beautiful_String(intNum,posNum))
			i+=1
		
		print("-"*Rovn)



	def Prepare_Beautiful_String(self,NumMass,PosMass):
		
		str_loto=""		
		
		k=0
		I=iter(PosMass)
		numIter=-1

		while True:
			try: 
				X = next(I) 		# Или I.__next__	
				numIter+=1	
			except StopIteration:					
				break

			while k<X:
				str_loto=str_loto+"   "
				k+=1

			str_loto=str_loto +'{:>3}'.format(str(NumMass[numIter]))  		# ВОТ ДЛЯ ЧЕГО УЧИЛИ! 
			k+=1

		return str_loto



	def Mark_Bochonok(self,NumMass,intBochonok):
		
		NewMass=[]

		for elem in NumMass:
			if elem==intBochonok:
				NewMass.append(SpecChar)
			else:
				NewMass.append(elem)
				# elem=SpecChar

		return NewMass
				# return NumMass
				# break



	def Check_Num_in_Card(self,NumMass,intBochonok):
		if Unic_value(NumMass,intBochonok)==True:
			return 2
		else:
			return 1

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""

print("")
print("="*15 + " "*5+ "Задача. Игра в лото")


History=[] 			#История выпавших боченков

# Константы задачи: карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр
a=3
b=5
c=9

User_Card=LotoCard(a,b,c,"Карточка пользователя")
Us_mass=User_Card.FillCard()

Comp_Card=LotoCard(a,b,c,"Карточка компьютера")
Comp_mass=Comp_Card.FillCard()


while True:
	User_Card.PrintCard(Us_mass[0],Us_mass[1])
	Comp_Card.PrintCard(Comp_mass[0],Comp_mass[1])


	while True:
		j=randint(Bound_l,Bound_u)
		if Unic_value(History,j)==True:
			History.append(j)
			break

	# Ожидаемое действие от пользователя
	ExpectAnsw=User_Card.Check_Num_in_Card(Us_mass[0],j)


	# Спросим пользователя
	Q=print("Выпал бочонок: ", j,"\nДля внесения в карточку нажмите [1], чтобы продолжить нажмите [2]")
	An=int(input("Ваше действие: "))


	# Сверим его ответ
	if An!=ExpectAnsw:
		print("Вы проиграли. Чуть больше внимательности... Дальше будет лучше, не расстраивайтесь!")
		break
	else:		
		Us_mass[0]=User_Card.Mark_Bochonok(Us_mass[0],j)		
		Comp_mass[0]= Comp_Card.Mark_Bochonok(Comp_mass[0],j)


	# if Comp_mass.Check_Num_in_Card(Comp_mass[0],j)==1: 
	# Comp_mass[0]=Comp_Card.Mark_Bochonok(Comp_mass[0],j)			#отметка от имени компьютера


	#Проверка не выиграл ли кто-то
	if MayBeWin(Us_mass[0])==True and MayBeWin(Comp_mass[0])==False:
		print("Ура, рады вместе с Вами! Поздравляем с победой над искусственным интеллектом!")
		break
	elif MayBeWin(Us_mass[0])==False and MayBeWin(Comp_mass[0])==True:
		print("Сегодня удача улыбнулась компьютеру! Вы проиграли!")
		break
	elif MayBeWin(Us_mass[0])==True and MayBeWin(Comp_mass[0])==True:
		print("Редкий случай! Ничья!")
		break

	print("Игра продолжается. Кличество ходов: ", len(History),". Выпавшие бочонки: ", History)
