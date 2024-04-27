# Задание 4
# Имеется папка с файлами
# Реализовать удаление файлов старше N дней
import os
import datetime

# Будем удалять файлы старше 3-х дней
n = 3


def check_delete(folder):
    # Обходим все вложенные папки
    for (root, dirs, files) in os.walk(folder, topdown=True):
        for f in files:
            file_path = os.path.join(root, f)
            last_modified = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            days_age = (datetime.datetime.now() - last_modified).days
            if days_age > n:
                # Удаляем
                os.remove(file_path)
                print("Файл {f} удален".format(f))


check_delete('test_folder')
