import os,shutil

# модуль подключается к ДЗ №5 для блока Normal

def ChangeFolder(preferPath):
	try:
		os.chdir(preferPath)
		print("Успешно изменено на " + preferPath)
	except Exception as e:
		print("ошибка при измении пути на " + preferPath)



def FolderConsist(InterestPath):
	
	if InterestPath=="":
		InterestPath=os.getcwd()

	List_all=[]
	List_all=os.listdir(InterestPath) 
	
	for Files in List_all:
		print(Files)



def CreateDir(DirName):
	
	new_dir=os.path.join(os.getcwd(),DirName)
	
	try:
		os.mkdir(new_dir)
		print("директория " + new_dir + " создана")
	except Exception as e:		# fileexistserror:
		print("возможно, директория " + new_dir + " существует")



def DelDir(DirName):
	
	new_dir=os.path.join(os.getcwd(),DirName)
	
	try:
		os.removedirs(new_dir)
		print("директория " + new_dir + " удалена")
	except Exception as e:	
		print("ошибка при удалении: " + new_dir )

