"""
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

"""


import json


def write_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as loaded_data:
        json_data = json.load(loaded_data)

    with open('orders.json', 'w', encoding='utf-8') as saved_orders:
        orders_list = json_data['orders']
        order_info = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date,
        }
        orders_list.append(order_info)
        json.dump(json_data, saved_orders, indent=4)


write_to_json('FIFA', '1', '599', 'John Doe', '10.02.2022')
