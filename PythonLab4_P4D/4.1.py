from moviepy.editor import VideoFileClip


def extract_video_segment(input_file, start_time, end_time, output_file):
    try:
        # Открываем видеофайл
        with VideoFileClip(input_file) as video:
            # Обрезаем видео по указанным времени начала и окончания
            video_segment = video.subclip(start_time, end_time)
            # Сохраняем фрагмент в новый файл
            video_segment.write_videofile(output_file, codec="libx264", audio_codec="aac")
    except Exception as e:
        print(f"An error has occurred: {e}")


# Пример использования программы
if __name__ == "__main__":
    input_file = r"C:\Videos\mountain.mp4"          # Имя входного файла
    start_time = 10                     # Время начала в секундах
    end_time = 20                       # Время окончания в секундах
    output_file = r"C:\Videos\mountain_output.mp4"  # Имя выходного файла

    extract_video_segment(input_file, start_time, end_time, output_file)