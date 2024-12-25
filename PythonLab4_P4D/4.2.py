from moviepy.editor import VideoFileClip
from skimage.transform import resize
import os
import numpy as np
from PIL import Image
import zipfile


def extract_frames(video_path, start_time, end_time, output_zip, frame_step=10):
    # Открываем видеоклип
    clip = VideoFileClip(video_path).subclip(start_time, end_time)

    # Создаем ZIP-архив для сохранения кадров
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        frame_number = 0  # Для именования кадров

        # Создаем временную директорию, если она не существует
        temp_dir = "temp_frames"
        os.makedirs(temp_dir, exist_ok=True)

        # Пробегаемся по всем кадрам в клипе с шагом
        for t in range(0, int(clip.duration * clip.fps), frame_step):
            # Получаем кадр в виде numpy массива
            frame = clip.get_frame(t / clip.fps)

            # Преобразуем кадр для изменения размера
            aspect_ratio = frame.shape[1] / frame.shape[0]
            new_height = int(250 / aspect_ratio)

            # Изменяем размер изображения до 250px по ширине, сохраняя соотношение сторон
            frame_resized = resize(frame, (new_height, 250), anti_aliasing=True)

            # Преобразуем массив в изображение
            frame_image = Image.fromarray((frame_resized * 255).astype(np.uint8))

            # Создаем имя файла для кадра
            frame_filename = os.path.join(temp_dir, f"{frame_number}.png")

            # Сохраняем изображение во временном файле
            frame_image.save(frame_filename)

            # Добавляем изображение в ZIP-архив
            zipf.write(frame_filename, arcname=f"{frame_number}.png")

            frame_number += 1

    clip.close()

    # Удаляем временную директорию и все ее содержимое
    for filename in os.listdir(temp_dir):
        os.remove(os.path.join(temp_dir, filename))
    os.rmdir(temp_dir)

    print(f"Frame extraction is complete. The frames are saved in a zip archive: {output_zip}")


# Пример вызова функции
video_path = r'C:\Videos\mountain.mp4'  # Используйте r'' для корректной обработки обратных слешей
start_time = 10  # Начало в секундах
end_time = 30  # Конец в секундах
output_zip = 'frames.zip'  # Имя выходного ZIP-архива
frame_step = 10  # Шаг извлечения кадров

extract_frames(video_path, start_time, end_time, output_zip, frame_step)
