'''# не смог  правильно оформить в фукцию данный код, чтобы она работала. Писал код через input() и проверял.
for index in range(1, 101):   # создали диапозон чисел нужные нам по заданию.
    string = str(index)  # полученный диапозон перевели в строки, т.к. функция list() не работает с целыми.
    lists = list(string)  # перевели последовательность в список, чтобы можно было работать, с каждым элементом списка по отдельности
    if int(lists[-1]) == 1 and index != 11: # далее создаём и проверяем условия.
        print(f'{index} процент')
    elif int(lists[-1]) > 1 and int(lists[-1]) <= 4:
        if  index> 10 and index <= 14:
            print(f'{index} процентов')
        else:
            print(f'{index} процента')
    else:
        print(f'{index} процентов')
'''

'''
for index in range(1, 101):
    if index == 1 and index != 11:
        print(f'{index} процент')
    elif index > 1 and index <= 4:
        print(f'{index} процента')
    elif index == 21 or index == 31 or index == 41 or index == 51 or index == 61 or index == 71 or index == 81 or index == 91:
        print(f'{index} процент')
    else:
        print(f'{index} процентов')
'''
def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    for index in range(1, 101):
        if index == 1 and index != 11:
            print(f'{index} процент')
        elif index > 1 and index <= 4:
            print(f'{index} процента')
        elif index == 21 or index == 31 or index == 41 or index == 51 or index == 61 or index == 71 or index == 81 or index == 91:
            print(f'{index} процент')
        else:
            print(f'{index} процентов')
    return transform_string #верните отформатированную строку'


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))