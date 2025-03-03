import re


def correct_file_names(file_name: str) -> list:
    """Функция которая принимает имя файла и возвращает список имен, содержащихся в файле"""
    with open("data/" + file_name, "r", encoding="utf-8") as names_file:
        names_file_list = names_file.read().split()
    new_file_list = list()
    for name_item in names_file_list:
        name_new = ""
        for symbol in name_item:
            if symbol.isalpha():
                name_new += symbol
        if name_new.isalpha():
            new_file_list.append(name_new)
    return new_file_list


def cyrillic_names(name_item: str) -> bool:
    """Функция которая определяет кирилицу"""
    return bool(re.search("[а-яА-Я]", name_item))


def filter_russian_names(names_file_list: list) -> list:
    """Функция позволяющие из списка имен получать только русские имена"""
    new_ru_name_list = list()
    for name_item in names_file_list:
        if cyrillic_names(name_item):
            new_ru_name_list.append(name_item)
    return new_ru_name_list


def filter_english_names(names_file_list: list) -> list:
    """Функция позволяющие из списка имен получать только английские имена """
    new_en_name_list = list()
    for name_item in names_file_list:
        if not cyrillic_names(name_item):
            new_en_name_list.append(name_item)
    return new_en_name_list


def save_names_in_file(file_name: str, data: str) -> None:
    """"Функция которая сохраняет имена и создает файл"""
    with open("data/" + file_name, "w", encoding="utf-8") as names_file:
        names_file.write(data)


new_list = correct_file_names("names.txt")

ru_names_list = filter_russian_names(new_list)
for name in ru_names_list:
    print(name)
print("\n")

en_names_list = filter_english_names(new_list)
for name in en_names_list:
    print(name)

save_names_in_file("russian_names.txt", "\n".join(ru_names_list))
save_names_in_file("english_names.txt", "\n".join(en_names_list))
