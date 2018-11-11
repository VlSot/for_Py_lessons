import re
import os
from random import randint

__author__ = 'Сотников Владимир А.'
print("Данный файл содержит решения ДЗ №4 для блока normal, автор", __author__)


# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# i=len(line)
# print("Длина строки = " + str(i))


# Задание ооочень непонятно сформулировано. Если я верно понял, то надо получить список, 
# в котором элементы только в нижнем регистре и разделоителем в этой строке по сути является любая буква в верхнем регистре

my_arr=[]

j=0
strtmp=""

while j<=len(line)-1:
       if line[j].islower():
              strtmp=strtmp+line[j]
       elif line[j].islower()==False and strtmp!="":
              my_arr.append(strtmp)
              strtmp=""
       j+=1

# Последний эл-т чтобы не забыть, вдргу маленький
if strtmp!="":  
       my_arr.append(strtmp)
       strtmp=""


# Про строки
# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html

# for elem in my_arr:
#        print(elem)


With_RE=re.split(r"[ABCDEFGHIKLMNOPQRSTVXYZ]",line)
With_RE=[elem for elem in With_RE if elem]

print(With_RE)
# for elem in With_RE:
#        print(elem)




# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
print("")
print("="*15)
print("Задача 2")

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'
'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'
'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'
'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'
'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'
'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'
'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'
'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'
'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'
'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'
'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'
'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'
'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'
'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'
'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'


my_arr=[]

j=0
strtmp=""
podryad=0

idx_High_letters=[]
idx_inter=-1

"""
Пробежимся по все строке и составим список с индексами,которые удовлетворяют в 1м приближении. Т.е. заглавне подряд идут более 2х раз
На выходе: список idx_High_letters  - набор индексов с которых начинаются заглавные и идут более 2х подряд
"""
while j<len(line_2):
       if line_2[j].isupper():
              if strtmp=="":
                     idx_inter=j              
              strtmp=strtmp+line_2[j]
              podryad+=1              
       elif line_2[j].islower():
              if idx_inter!=-1 and podryad>2:
                     idx_High_letters.append(idx_inter)
              strtmp=""
              idx_inter=-1
              podryad=0
       else:
              idx_inter=-1
              podryad=0
       j+=1


# Выкинем теперь из этого списка все элементы у которых слева не две маленькие буквы

j=len(idx_High_letters)-1

while j>=0:
       mystr=line_2[idx_High_letters[j]-2:]
       if mystr[0].isupper() or mystr[1].isupper():
              idx_High_letters.pop(j)
       j-=1


# И еще одно дейсвие, когда каждый индекс необходимо преобразовать в эл-т списка, в вырезку из строки
idx=0
for elem in idx_High_letters:
      
       j=elem
       while line_2[j].isupper():
              j+=1
       idx_High_letters[idx]=line_2[elem:j-2]
       idx+=1


for elem in idx_High_letters:
       print(elem)

# мало не показалось, ковыряться с этой задачей... 

print("Или через RE: ")
With_RE=re.findall(r"[a-z]{2}([A-Z]+)[A-Z]{2}",line_2)
for elem in With_RE:
       print(elem)



# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

print("="*15)
print("Задача 3")

def Sum_elem(Mystr):
       num=0
       for elem in Mystr:
              num=num+int(elem)

       return num



Limit_g=2500

f = open('ForNumber.txt','w')
j=0
while j<Limit_g:
       f.write(str(randint(0,9)))
       j+=1 
f.close()


f = open('ForNumber.txt','r')
line_3=f.read()
f.close()

Chk_lst=[]

j=4 
while j<Limit_g:
       str_tmp=line_3[j-4:j]
       s=Sum_elem(str_tmp)
       
       my_l=[]
       my_l.append(j-4)
       my_l.append(s)

       Chk_lst.append(my_l)
       j+=1


Max_idx=Chk_lst[0][0]
Max_num=Chk_lst[0][1]

j=0
for elem in Chk_lst:
       if elem[1]>Max_num:
              Max_idx=Chk_lst[j][0]
              Max_num=Chk_lst[j][1]
       j+=1


print("Максимальное значение на позиции " + str(Max_idx) + " и составляет " + str(Max_num))

