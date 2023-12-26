import json

def get_data():
    '''Функция извлекает данные из файла operation.json и возвращает их'''
    with open(DATA_DIR, 'r') as file:
        json_data = file.read()

    data = json.loads(json_data)
    return data
