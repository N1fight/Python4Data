from PIL import Image
import os

# Загрузка изображения
img = Image.open('images/input/image.jpg')

# Разделяем изображение на отдельные каналы R, G, B
red_ch, green_ch, blue_ch = img.split()

# Создаем новое изображение с оригинальным изображением и отдельными каналами
width, height = img.size
new_img = Image.new('RGB', (width * 4, height))
new_img.paste(img, (0, 0))
new_img.paste(red_ch, (width, 0))
new_img.paste(green_ch, (width * 2, 0))
new_img.paste(blue_ch, (width * 3, 0))

# Отображаем новое изображение
new_img.show()

# Создаем папку для вывода, если она не существует
if not os.path.exists('images/output'):
    os.makedirs('images/output')

# Сохраняем новое изображение в папку
new_img.save('images/output/image_with_channels.jpg')