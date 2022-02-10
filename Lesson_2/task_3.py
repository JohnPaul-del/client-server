"""
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим
в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию
файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""


import yaml
from pprint import pprint


def write_to_yaml(file_name):

    some_data = {
        "brand": ["adidas", 'puma', 'nike'],
        'number': 999,
        "dict": {
            '1€': 1,
            '2$': 2,
            '3₽': 3
            },
        }

    with open(file_name, 'w', encoding='utf-8') as wf:
        yaml.dump(some_data, wf, default_flow_style=False, allow_unicode=True)

    with open(file_name,  encoding='utf-8') as rf:
        loaded_data = yaml.load(rf, yaml.Loader)

    pprint(some_data == loaded_data)


write_to_yaml('test.yaml')
