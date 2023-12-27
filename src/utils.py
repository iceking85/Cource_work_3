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

def sorted_date():
    '''Сортировка по датам'''
    sorted_dict = sorted_executed()
    sorted_data = sorted(sorted_dict, key=lambda x: x['date'], reverse=True)
    result = []
    for i in sorted_data:
        result.append(i)
    return result

def first_five_operations():
    '''Получаем первые 5 словарей'''
    sorted_date_dict = sorted_date()
    first_five_dicts = sorted_date_dict[:5]
    return first_five_dicts


