# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.
#
#
# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
#
#
# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
# Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.
#
#
# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).
#
#
# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый
# тип на кириллице.
#
#
# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Далее забыть о том, что мы сами только что создали этот файл и исходить из того, что перед нами файл
# в неизвестной кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был
# создан.


import subprocess


words = ["разработка", "декоратор", "сокет"]
u_words = [
    "\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430",
    "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440",
    "\u0441\u043e\u043a\u0435\u0442"
]
print(f'{"#"*10} - TASK-1 - {"#"*10}')
[print(f'{el} - {type(el)}') for el in words]
[print(f'{el} - {type(el)}') for el in u_words]


b_words = [b'class', b'function', b'method']
print(f'\n{"#"*10} - TASK-2 - {"#"*10}')
[print(f'{el} - {type(el)} - {len(el)}') for el in b_words]

nb_words = ["attribute", "класс", "функция", "type"]
print(f'\n{"#"*10} - TASK-3 - {"#"*10}')
[print(f'{el} - impossible to write in ASCII format') for el in nb_words if len(el.encode('ascii', 'ignore')) == 0]

d_words = ["разработка", "администрирование", "protocol", "standard"]
print(f'\n{"#"*10} - TASK-4 - {"#"*10}')
for el in d_words:
    e_word = el.encode('utf-8')
    print(f'Encode: {e_word} - {type(e_word)}')
    d_word = e_word.decode('utf-8')
    print(f'Decode: {d_word} - {type(d_word)}')


# w_sites = [
#     ['ping', 'google.com'],
#     ['ping', 'yandex.ru']
# ]
# print(f'\n{"#"*10} - TASK-5 - {"#"*10}')
# for w_site in w_sites:
#     subprocess_ping = subprocess.Popen(w_site, stdout=subprocess.PIPE)
#     for el in subprocess_ping.stdout:
#         el = el.decode('cp866').encode('utf-8')
#         print(f'{el.decode("utf-8")}')


f_words = ["сетевое программирование", "сокет", "декоратор"]
with open('file.txt', 'w') as f:
    [f.writelines('\r'+el) for el in f_words]

print(f'\n{"#"*10} - TASK-6 - {"#"*10}')
with open('file.txt', 'r') as f:
    print(f'Default: {f.read()}')
with open('file.txt', 'r', encoding='utf-8', errors='replace') as f:
    print(f'In UTF-8: {f.read()}')

"""    
В данном случае оба раза без каких либо ошибок. Подозреваю, что из-за пуссифицированного Linux, 
у которого по умолчанию кодировка UTF-8
"""