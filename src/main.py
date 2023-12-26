from utils import first_five_operations


list_five_last_operations = first_five_operations()


def main():
    for i in list_five_last_operations:
        print(f"{i['date'][:10]} {i['description']}")
        if i['description'] == 'Открытие вклада':
            print(f"> Счет {'****'}{i['to'][-4:]}")
            print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
            print('------')
        elif i['description'] == 'Перевод организации':
            print(f"{i['from'][0:-16]} {'****'}{i['from'][-4:]}-> {'Счет ****'}{i['to'][-4:]}")
            print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
            print('------')
        elif i['description'] == 'Перевод со счета на счет':
            print(f"От: {'****'}{i['from'][-4:]} -> {'Счет ****'}{i['to'][-4:]}")
            print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
            print('------')
    return



if __name__ == '__main__':
    main()