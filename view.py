def view_info(data: list):
    if len(data) > 0:
        print(f'Фамилия: {data[0]}, телефон: {data[1]}')
    else:
        print('Нет данных')


def get_info(field: str) -> str:
    if field == 'fio':
        return input('Введите фамилию: ')
    else:
        return input('Введите телефон: ')
