# Задание 6*
# Имеется банковское API возвращающее JSON
# {
#     "Columns": ["key1", "key2", "key3"],
#     "Description": "Банковское API каких-то важных документов",
#     "RowCount": 2,
#     "Rows": [
#         ["value1", "value2", "value3"],
#         ["value4", "value5", "value6"]
#     ]
# }
# Основной интерес представляют значения полей "Columns" и "Rows",
# которые соответственно являются списком названий столбцов и значениями столбцов
# Необходимо:
#     1. Получить JSON из внешнего API
#         ендпоинт: GET https://api.gazprombank.ru/very/important/docs?documents_date={"начало дня сегодня в виде таймстемп"}
#         (!) ендпоинт выдуманный
#     2. Валидировать входящий JSON используя модель pydantic
#         (из ТЗ известно что поле "key1" имеет тип int, "key2"(datetime), "key3"(str))
#     2. Представить данные "Columns" и "Rows" в виде плоского csv-подобного pandas.DataFrame
#     3. В полученном DataFrame произвести переименование полей по след. маппингу
#         "key1" -> "document_id", "key2" -> "document_dt", "key3" -> "document_name"
#     3. Полученный DataFrame обогатить доп. столбцом:
#         "load_dt" -> значение "сейчас"(датавремя)
# *реализовать п.1 с использованием Apache Airflow HttpHook

# 1  APACHE AIRFLOW
# import datetime
# from airflow import DAG
# from airflow.hooks.http_hook import HttpHook
# from airflow.operators.python_operator import PythonOperator
#
# def get_data(*args, **kwargs):
#     api_hook = HttpHook(http_conn_id="api_connection", method='GET')
#     data_dict = {}
#
#     endpoint_url = "https://api.gazprombank.ru/very/important/docs?documents_date=".format(datetime.datetime.today().strftime("%s"))
#
#     resp_url = api_hook.run(endpoint=endpoint_url)
#     resp = json.loads(resp_url.content)
#
#     with open("D:\apache_airflow/res.json", "w") as f:
#         json.dump(result, f)
#     f.close()
#
# dag = DAG(
# 	'gazprom_api',
# 	start_date = datetime.datetime.now()
# 	# max_active_runs = 1
# 	)
#
#
#
# get_data_api = PythonOperator(
# 					task_id = 'get_data',
# 					python_callable = get_data,
# 					dag = dag)
from datetime import datetime

import pandas as pd

income_json = {
    "Columns": ["key1", "key2", "key3"],
    "Description": "Банковское API каких-то важных документов",
    "RowCount": 2,
    "Rows": [
        [1, "2024-01-02", "value3"],
        [2, "value5", "value6"]
    ]
}

# 2 Валидировать входящий JSON используя модель pydantic (из ТЗ известно что поле "key1" имеет тип int, "key2"(datetime), "key3"(str))
from pydantic import BaseModel, validator


class Values(BaseModel):
    key1: int
    key2: datetime
    key3: str


data = [dict(zip(income_json['Columns'], x)) for x in income_json["Rows"]]
for val in data:
    print('Валидация данных "{}"'.format(val))
    try:
        valid_result = Values(**val)
        print(valid_result)
    except ValueError as e:
        print(e.errors())

# 2. Представить данные "Columns" и "Rows" в виде плоского csv-подобного pandas.DataFrame
df = pd.DataFrame(data)
print('Данные в  DataFrame\n {}'.format(df))

# 3. В полученном DataFrame произвести переименование полей по след. маппингу
# "key1" -> "document_id", "key2" -> "document_dt", "key3" -> "document_name"
columns = {"key1": "document_id", "key2": "document_dt", "key3": "document_name"}
df = df.rename(columns=columns)
print('Переименованный DataFrame\n {}'.format(df))

# 3. Полученный DataFrame обогатить доп. столбцом:
# "load_dt" -> значение "сейчас"(датавремя)
df['значение "сейчас"'] = datetime.now()
print('Обогащенный DataFrame\n {}'.format(df))