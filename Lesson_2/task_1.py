""""
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции
создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета
в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также
оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""

import csv
import re
from pprint import pprint


def get_data_from_csv(csv_files):
    result = []
    re_values = re.compile(r'^(Изготовитель системы|Название ОС|Код продукта|Тип системы)')

    for item in csv_files:
        res = {}
        with open(item, 'r', encoding='windows-1251') as f:
            for els in f:
                values = els.split(':')
                for el in values:
                    if re_values.search(el):
                        res[el] = values[1].strip()
            result.append(res)
    return result


def write_to_csv(csv_file='data_report.csv'):
    data = get_data_from_csv(['info_1.txt', 'info_2.txt', 'info_3.txt'])
    data_cols = data[0].keys()
    with open(csv_file, 'w', encoding='utf8') as data_file:
        writer = csv.DictWriter(data_file, data_cols)
        writer.writeheader()
        writer.writerows(data)


write_to_csv()
# pprint(get_data_from_csv(['info_1.txt', 'info_2.txt', 'info_3.txt']))
