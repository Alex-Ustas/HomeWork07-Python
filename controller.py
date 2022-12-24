import logger
import view
import search


def select_func():
    print('1 - Найти контакт')
    print('2 - Добавить контакт в базу')
    print('0 - Закончить')
    while True:
        action = input('Выберите действие: ')
        if action == '1':
            data = view.get_info('fio')
            base = logger.get_base()
            view.view_info(search.search_result(base, data))
        elif action == '2':
            data = list()
            data.append(view.get_info('fio').capitalize())
            data.append(view.get_info('phone'))
            logger.add_to_base(data)
        elif action == '0':
            break
        else:
            print('Выбрано неверное действие')
        print('')
