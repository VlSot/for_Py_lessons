import os,shutil


__author__ = 'Сотников Владимир А.'
print("Данный файл содержит решения ДЗ №5 для блока easy, автор", __author__)



# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
print("="*15 + " "*5+ "Задача 1")
j=0
while j<=9:
	
	new_dir=os.path.join(os.getcwd(),"dir_"+str(j))
	
	try:
		os.mkdir(new_dir)
		print("директория " + new_dir + " создана")
	except Exception as e:		# fileexistserror:
		print("директория " + new_dir + " существует")
	finally:
		j+=1
	
#Удаление
j=0
while j<=9:

	new_dir=os.path.join(os.getcwd(),"dir_"+str(j))

	try:
		os.removedirs(new_dir)
		print("директория " + new_dir + " удалена")
	except Exception as e:		# fileexistserror:
		print("ошибка при удалении: " + new_dir )
	finally:
		j+=1





# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print("")
print("="*15 + " "*5+ "Задача 2")

List_all=[]
List_all=os.listdir() 

print("Папки в текущей директории: ")
for Folder in List_all:
	if os.path.isfile(Folder)==False:
		print(Folder)




# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
print("")
print("="*15 + " "*5+ "Задача 3")


ll=[]
ll=os.path.split(__file__)

file_path=os.path.join(ll[0],"copy_" + ll[1])

if os.path.exists(file_path):
	print('Похоже, копия уже существует')
else:
	shutil.copy(__file__,file_path)
	print('Копия создана под именем '+"copy_" + ll[1])
