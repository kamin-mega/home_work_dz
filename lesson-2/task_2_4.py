'''
list_in = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for element in list:
    print(f"Привет, {element.split()[-1].title()}!")
'''

def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    # пишите реализацию своей программы здесь
    list_out = []
    for element in list_in:
        transformation_element = f"Привет, {element.split()[-1].title()}!"
        list_out.append(transformation_element)
    #list_out =  ["здесь должены оказаться результирующие строковые приветствия"]
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)
