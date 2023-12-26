from config import OPERATIONS_FILE
import json

def get_all_operations():
    '''Функция извлекает данные из файла operations.json и возвращает их'''
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return(data)

def filtered_operations():
    '''Функция фильтрует словари от пустого'''
    list_of_dicts = get_all_operations()
    filtered_list = list(filter(lambda x: x, list_of_dicts))
    return filtered_list

def sorted_executed():
    '''сортируем по операциям (EXECUTED)'''
    executed_list = []
    filter_list = filtered_operations()
    for i in filter_list:
        if i['state'] == "EXECUTED":
            executed_list.append(i)
        else:
            continue
    return executed_list

