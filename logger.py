def get_base() -> dict:
    with open('phones.csv', 'r', encoding='utf-8-sig') as file:
        line = file.readline().replace('\n', '').replace('\r', '')
        base = dict()
        base[0] = line.split(';')
        count = 1
        while line:
            line = file.readline().replace('\n', '').replace('\r', '')
            base[count] = line.split(';')
            count += 1
    return base


def add_to_base(data: list):
    with open('phones.csv', 'a', newline='', encoding='utf-8') as file:
        file.write(f'{data[0]};{data[1]}\n')
