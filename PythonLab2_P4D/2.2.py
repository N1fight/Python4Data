from PIL import Image
from sys import argv

# Проверяем, был ли передан путь к изображению в качестве аргумента командной строки
if(len(argv) > 1):
    image_path = argv[1]
else:
    print("Enter a path to your image!")
    exit()

# Инициализируем переменные для суммирования значений цветовых каналов
red_ch, green_ch, blue_ch = 0, 0, 0

# Открываем изображение и загружаем пиксели
with Image.open(image_path) as img:
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            # Суммируем значения цветовых каналов для каждого пикселя
            red_ch += pixels[x, y][0]
            green_ch += pixels[x, y][1]
            blue_ch += pixels[x, y][2]

# Определяем преобладающий цвет
maxNum = "R" if red_ch > green_ch else "G"
maxNum = "G" if green_ch > blue_ch else "B"

# Выводим результат
print(maxNum, "-", max(red_ch, green_ch, blue_ch))