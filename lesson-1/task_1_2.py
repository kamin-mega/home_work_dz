"""# a
cubes = [numbers ** 3 for numbers in range(1, 1001, 2)]  # создал список кубов
sum_one_number = 0
sum_numbers = 0
for indx in cubes:                                   # Цикл for производит перебор элементов списка
    i = indx                                         # While производит разбиение числа на отдельные числа, и провзодит сложение
    while i > 0:                                     # Далее производиться проверка делимости и сложение прошедших условие чисел.
        digit = i % 10                               #
        sum_one_number = sum_one_number + digit
        i = i // 10
    if sum_one_number % 7 == 0:
        sum_number = sum_numbers + i
        sum_one_number = 0
print(sum_numbers)
"""
# b
"""
cubes = [(numbers ** 3) + 17 for numbers in range(1, 1001, 2)] создал список кубов  и прибавил 17
sum_one_number = 0
sum_one_number = 0
sum_numbers = 0
for indx in cubes:
    i = indx
    while i > 0:
        digit = i % 10
        sum_one_number = sum_one_number + digit
        i = i // 10
    if sum_one_number % 7 == 0:
        sum_number = sum_numbers + i
        sum_one_number = 0
print(sum_numbers)
"""

def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    sum_digits = 0
    sum_num = 0
    for i in dataset:
        indx = i
        while indx > 0:
            digit = indx % 10
            sum_digits = sum_digits + digit
            indx = indx // 10
        if sum_digits % 7 == 0:
            sum_num = sum_num + i
        sum_digits = 0
    return sum_num  # Верните значение полученной суммы


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    for i in range(len(dataset)):
        dataset[i] = dataset[i] + 17
    return sum_list_1(dataset)  # Верните значение полученной суммы


my_list = [numbers ** 3 for numbers in range(1, 1001, 2)]  # Соберите нужный список по заданию
print(my_list)
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)