# Импортируем 2 модуля
import argparse
import os

# Создаём объект parser и 2 аргумента dirpath и files
parser = argparse.ArgumentParser()
parser.add_argument('--dirpath', default='.')
parser.add_argument('--files', nargs='*', default='')

#парсинг аргументов
#присваиваем перееменным значения аргументов
Parser_Args = parser.parse_args()
source_path = Parser_Args.dirpath
files = Parser_Args.files

#два пустых списка существующих и несуществующих файлов
exist_files = []
not_exist_files = []
#список файлов в директории указанной в аргументе --dirpath, с помощью метода listdir()
dir_files = os.listdir(source_path)

#цикл проходящий по файлам, если список не пустой.
#проверяет их наличие в директории и распределяет их по спискам
if(len(files) != 0):
    for file in files:
        check = 0
        for exist in dir_files:
            if (file == exist):
                check = 1
                break
        if (check):
            exist_files.append(file)
        else:
            not_exist_files.append(file)

#открываем два файла, проходим по циклу
#для каждого файла выводится информация на экран и записывается в соответствующий файл
    with open('exist.txt', 'w') as exist, open('notExist.txt', 'w') as notExist:
        print("exist files:")
        for i in exist_files:
            print(f'{i}')
            exist.write(f'{i}\n')

        print("not exist files:")
        for i in not_exist_files:
            print(f'{i}')
            notExist.write(f'{i}\n')

#Если список файлов пустой, считаем кол-во файлов в директории и размер файлов
else:
    numOfSourcesFiles = len(dir_files)
    sum = 0
    for i in dir_files:
        sum += os.path.getsize(f'{source_path}/{i}')
    print(f'This directory contains {numOfSourcesFiles} files and has a total size: {sum} bytes')