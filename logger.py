def get_base() -> dict:
    with open('phones.csv', 'r', newline='', encoding='utf-8') as file:
        count = 0
        line = file.readline().replace('\n', '').replace('\r', '')
        base = dict()
        base[0] = line.split(';')
        while line:
            line = file.readline().replace('\n', '').replace('\r', '')
            base[count] = line.split(';')
            count += 1
    return base


def add_to_base(fio: str, phone: str):
    with open('phones.csv', 'a', newline='', encoding='utf-8') as file:
        file.write(f'{fio};{phone}')
