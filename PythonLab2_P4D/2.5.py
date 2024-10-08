from PIL import Image
from argparse import ArgumentParser
from pathlib import Path

# Создаем парсер аргументов командной строки
Argument_Parser = ArgumentParser()
Argument_Parser.add_argument("-ftype")  # добавляем аргумент для указания формата изображения
format = Argument_Parser.parse_args().ftype  # получаем значение аргумента

# Указываем путь к директории с изображениями
path = Path("images/change format image")

# Перебираем все файлы в директории
for i in path.iterdir():
    try:
        # Открываем изображение с помощью PIL
        with Image.open(i) as img:
            # Проверяем, является ли формат изображения указанным в аргументе
            if img.format.lower() == format:
                # Изменяем размер изображения до 50x50 пикселей
                new = img.resize((50, 50))
                # Отображаем измененное изображение
                new.show()
    except:
        pass