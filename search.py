def search_result(base: dict, fio: str) -> list:
    for person in base.values():
        if person[0].lower() == fio.lower():
            return person
    return list()
