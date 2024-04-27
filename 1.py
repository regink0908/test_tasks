# Задание 1
# имеется текстовый файл f.csv, по формату похожий на .csv с разделителем |
"""
lastname|name|patronymic|date_of_birth|id
Фамилия1|Имя1|Отчество1 |21.11.1998   |312040348-3048
Фамилия2|Имя2|Отчество2 |11.01.1972   |457865234-3431
...
"""
# 1. Реализовать сбор уникальных записей
# 2. Случается, что под одинаковым id присутствуют разные данные - собрать такие записи

from faker import *
import pandas as pd

fake = Faker(['ru-RU'])


# Генерируем данные
def generate_data():
    with open('src/f.csv', 'a', encoding='utf-8') as f:
        for _ in range(150):
            try:
                lastname, name, patronymic = fake.name().split()
                date_of_birth = fake.date_of_birth().strftime('%d.%m.%Y')
                id = fake.pystr_format('#########-{{random_int}}')
                f.write('|'.join([lastname, name, patronymic, date_of_birth, id]) + '\n')
            except:
                pass


# Генерируем данные, если необходимо
# generate_data()


# Считываем файл в DataFrame
df = pd.read_csv('src/f.csv', delimiter='|')
df_unique = df.drop_duplicates()

df_common_id = df[df.duplicated(['id'])].drop_duplicates()

print('1. Всего записей:{}.\nУникальных записей: {}'.format(df.shape[0], df_unique.shape[0]))
print('2. Различные записи с одинаковым id:\n',df_common_id)