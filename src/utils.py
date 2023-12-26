from config import OPERATIONS_FILE
import json

def get_all_operations():
    '''Функция извлекает данные из файла operations.json и возвращает их'''
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return(data)
