# a вывод списка.


def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    # пишите реализацию своей программы здесь
    end_list = []
    for element in list_in:
        if element[0] in ['+'] or element.isdigit():
            if element.isdigit:
                end_list.append(f'"{element.zfill(2)}"')
            else:
                end_list.append(f'"{element[0]}{element[1:-1]}"')
        else:
             end_list.append(element)

    str_out = end_list#"здесь полученная после всех преобразования строковая переменная"
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(type(result), result)


# b  вывод  строки


def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    # пишите реализацию своей программы здесь
    end_list = []
    for element in list_in:
        if element[0] in ['+'] or element.isdigit():
            if element.isdigit:
                end_list.append(f'"{element.zfill(2)}"')
            else:
                end_list.append(f'"{element[0]}{element[1:-1]}"')
        else:
             end_list.append(element)

    str_out = ' '.join(end_list)#"здесь полученная после всех преобразования строковая переменная"
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(type(result), result)

