#импортируем 2 модуля
from sys import argv
import os

#создаём переменную для указания пути к директорию, содержащему файл "NotExist.txt"
path = '.'
if(len(argv) > 1):
    path = argv[1]

#метод, который создаёт файл в path, если он не существует.
#если каталок существует, не будет генерироваться ошибки
os.makedirs(path, exist_ok=True)

# Открываем файл и разбивается на строки с помощью метода splitlines()
with open('notExist.txt', 'r') as file:
    files = file.read().splitlines()

#пробегаем циклом по строкам в списке files
#для каждой строки формируем полный путь к файлу
#открываем файл
#с помощью with файл закрывается, оставаясь пустым
for fileName in files:
    dir_path = os.path.join(path, fileName)
    with open(dir_path, "w"):
        pass