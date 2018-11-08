import module_for_05normal as Sotych


__author__ = 'Сотников Владимир А.'
print("Данный файл содержит решения ДЗ №5 для блока Normal, автор", __author__)


def WhatWeCan():
	print("\nВыберите: ")
	num=input(" 1 - для изменения рабочего каталога; \n 2 - просмотр содержимого каталога; \n 3 - создание директории; \n 4 - удаление директории ; \n\n 0 - выход\n Ваш выбор: ")
	return num



print("Программа позволяет короткими командами работать с файлами. ")
Num_Ex=-1

while Num_Ex!=0:
	Num_Ex=WhatWeCan()

	if int(Num_Ex)==0:
		break

	if int(Num_Ex)==1:		#изменение каталога
		pth=input("Введите новый путь: ")
		Sotych.ChangeFolder(pth)
	
	if int(Num_Ex)==2:		#содержание каталога
		pth=input("Укажите путь для построения содержимого \n(пустой параметр вернет содержание рабочего каталога)): ")
		Sotych.FolderConsist(pth)

	if int(Num_Ex)==3:		#создать директорию в рабочем каталоге
		pth=input("Имя создаваемой директории в рабочей папке: ")
		Sotych.CreateDir(pth)

	if int(Num_Ex)==4:		#Удалить каталог
		pth=input("Имя удаляемой директории: ")
		Sotych.DelDir(pth)


