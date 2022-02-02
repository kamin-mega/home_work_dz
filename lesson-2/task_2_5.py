# Сам поробывал решить задание а. 

'''

import random
indx = 0
new_list = []
one_list = []
while indx < 7:
    random_digits = random.uniform(1, 100)
    random_digits_int = random.randint(1, 100)
    random_digits = round(random_digits, 2)
    new_list.append(random_digits_int)
    new_list.append(random_digits)
    indx += 1
for some_indx in new_list:
    some_indx = float(some_indx)
    rub = int(some_indx * 100) // 100
    kop = int(some_indx * 100) % 100
    my_price = f'{rub} руб {kop:.2f} коп'
    one_list.append(my_price)
    final_str = ','.join(one_list)

print(final_str)

'''

from random import uniform

# a


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и 
        формирует из них единую строковую переменную разделяя значения запятой."""
    # пишите реализацию своей программы здесь
    one_list = []
    for some_indx in list_in:
        some_indx = float(some_indx)
        rub = int(some_indx * 100) // 100
        kop = int(some_indx * 100) % 100
        my_price = '{0} руб {1:02d} коп, '.format(rub, kop)
        one_list.append(my_price)
    print('ID =', id(one_list),type(one_list))
    str_out = one_list #"здесь итоговая строка"
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)

print('\n\n')

# b цены отсортированные по возрастанию

def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    # пишите реализацию своей программы здесь
    one_list = []
    for some_indx in list_in:
        some_indx = float(some_indx)
        rub = int(some_indx * 100) // 100
        kop = int(some_indx * 100) % 100
        my_price = '{0} руб {1:02d} коп, '.format(rub, kop)
        one_list.append(my_price)
        one_list.sort()
    print('ID =', id(one_list),type(one_list))
    str_out = one_list #"здесь итоговая строка"
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)

print('\n\n')

# c список, содержащий те же цены, но отсортированные по убыванию.

def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    # пишите реализацию своей программы здесь
    one_list = []
    for some_indx in list_in:
        some_indx = float(some_indx)
        rub = int(some_indx * 100) // 100
        kop = int(some_indx * 100) % 100
        my_price = '{0} руб {1:02d} коп, '.format(rub, kop)
        one_list.append(my_price)
        one_list.sort(reverse = True)
    print('ID =', id(one_list),type(one_list))
    str_out = one_list #"здесь итоговая строка"
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)

print('\n\n')

# d вывод 5 максимальных.

def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    # пишите реализацию своей программы здесь
    one_list = []
    for some_indx in list_in:
        some_indx = float(some_indx)
        rub = int(some_indx * 100) // 100
        kop = int(some_indx * 100) % 100
        my_price = '{0} руб {1:02d} коп, '.format(rub, kop)
        one_list.append(my_price)
        one_list.sort(reverse = True)
        maximum =one_list[0:5]
    str_out = maximum #"здесь итоговая строка"
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)
