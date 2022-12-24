import logger
import view
import search


def select_func():
    print('1 - Найти контакт')
    print('2 - Добавить контакт в базу')
    action = int(input('Выберите действие: '))
    if action == 1:
        data = view.get_info()
        base = logger.get_base()
        print(search.search_result(base, data))
    else:
        data = view.get_info()
        print(data)
