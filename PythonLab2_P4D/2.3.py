from PIL import Image, ImageDraw, ImageFont

# Функция для добавления водяного знака к изображению
def Add_watermark(in_Image_Path, in_Watermark_Image_Path, out_Image_Path, watermark_Text, pos_Image, pos_Text):
    # Открываем исходное изображение и изображение водяного знака
    with Image.open(in_Image_Path) as img, Image.open(in_Watermark_Image_Path) as new_img:
        # Создаем объект для рисования на изображении
        output = ImageDraw.Draw(img)

        # Изменяем размер изображения водяного знака до 200x200 пикселей
        new_img = new_img.resize((100, 100))

        # Вставляем изображение водяного знака в исходное изображение на заданной позиции
        img.paste(new_img, pos_Image)

        # Создаем объект для рисования текста на изображении
        draw_img = ImageDraw.Draw(img)

        # Загружаем шрифт по умолчанию с размером 30 пикселей
        font_text = ImageFont.load_default(size=30)

        # Добавляем текст водяного знака на изображение на заданной позиции
        draw_img.text(pos_Text, watermark_Text, fill=(90, 0, 90), font=font_text)

        # Показываем полученное изображение
        img.show()

        # сохраняем полученное изображение в файл
        img.save(out_Image_Path, "jpeg")

if __name__ == '__main__':
    # Путь к исходному изображению
    input_Image_Origin_Path = "images/input/image.jpg"

    # Путь к изображению водяного знака
    input_Image_with_Watermark_Path = "images/input/image_with_watermark.jpg"

    # Путь к файлу для сохранения результата
    output_Image_Result_Path = "images/output/result_image_with_watermark.jpg"

    # Вызываем функцию watermark с параметрами
    Add_watermark(input_Image_Origin_Path, input_Image_with_Watermark_Path, output_Image_Result_Path, watermark_Text='TulinovKonstanitn_P4D', pos_Image=(10, 10), pos_Text=(10, 10))