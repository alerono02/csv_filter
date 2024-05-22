from src.func import *


def start_script(data):
    global new_data
    while True:
        choice = int(input("\nВыберите действие:\n"
                           "1 - Подсчёт числа действий каждого клиента.\n"
                           "2 - Фильтрация данных по критериям.\n"
                           "3 - Среднее число действий клиентов и топ-5 клиентов с наибольшими действиями.\n"
                           "4 - Сохранение файла.\n"
                           "5 - Выход.\n"))
        # print(data['action'].unique()) # названия действий
        match choice:
            case 1:
                new_data = count_actions(data)
                print(new_data, '\n')
            case 2:
                print('Выберите критерий:')
                i = 0
                columns = data.columns.values.tolist()
                for col in columns:
                    print(f'{i} - {col}')
                    i += 1
                choice = int(input())
                column = columns[choice]
                match choice:
                    case 1:
                        print("Выберите 'action': ")
                        i = 0
                        for action in data['action'].unique():
                            print(f'{i} - {action}')
                            i += 1
                        choice = int(input())
                        filter_param = data['action'].unique()[choice]
                        new_data = filter_data(data, column, filter_param)
                    case _:
                        filter_param = input(f'Введите {column}: ')
                        new_data = filter_data(data, column, filter_param)
                print(new_data, '\n')
            case 3:
                new_data = analyze_client_behavior(data)
                print(new_data)
            case 4:
                filename = input('Введите название файла без формата: ')
                format_file = input('Введите формат файла(csv, excel, xml, json): ')
                save_data(new_data, filename, format_file)
            case 5:
                exit()
            case _:
                print('Введите число!\n')