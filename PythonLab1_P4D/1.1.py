# Импортируем три модуля
import os
from shutil import copy
from sys import argv

#создаём переменную для указания пути к директорию, содержащему файлы для обработки
Source_Path = '.'
if(len(argv) > 1):
    Source_Path = argv[1]

#создаём переменную files для хранения списка файлов в директории "SourcePath"
#создаём переменную listofFiles для хранения файлов по размеру <= 2К
files = os.listdir(Source_Path)
list_of_files = []

#инициализируем цикл, который проходит по размерам файлов и сравнивает их с 2К. Обновляем список
for i in files:
    file_size = os.path.getsize(f'{Source_Path}/{i}')
    if file_size <= 2048:
        list_of_files.append(i)

#условие: если длина списка не ноль создаём директорий small.
#в случае его существования срабатывает исключение

if len(list_of_files) != 0:
    try:
        os.mkdir("small")
    except FileExistsError:
        print("The directory already exists")

#перебираем список, для каждого файла создаём исходный и целевой пути.
#копируем каждый файл из исходного в целевой.
#если файлы не найдены, выводит сообщение в консоль
    for i in list_of_files:
        file_Source_Path = f'{Source_Path}/{i}'
        file_Destination_Path = "small/" + str(i)
        copy(file_Source_Path, file_Destination_Path)
else:
    print("The are no such files")