from PIL import Image, ImageDraw, ImageFont

# Цикл для создания изображений с номерами от 1 до 3
for i in range(1, 4):
    # Задаем размеры изображения (100x100 пикселей)
    width, height = 100, 100

    # Создаем новое изображение с белым фоном
    img = Image.new('RGB', (width, height), 'white')

    # Создаем инструмент для рисования на изображении
    draw = ImageDraw.Draw(img)

    # Рисуем синий квадрат по краям изображения
    draw.line([(0, 0), (100, 0), (100, 100), (0, 100), (0, 0)], width=5, fill=(0, 0, 255))

    # Загружаем шрифт по умолчанию с размером 40 пикселей
    font = ImageFont.load_default(40)

    # Определяем позицию текста в центре изображения
    text_Pos = (width // 2, height // 2)

    # Выводим текст (номер изображения) в центре изображения красным цветом
    draw.text(text_Pos, str(i), anchor="mm", font=font, fill='red')

    # Отображаем изображение на экране
    img.show()

    # Сохраняем изображение в папке "images" с именем "i.png"
    img.save(f"images/output/{i}.png", format="png")