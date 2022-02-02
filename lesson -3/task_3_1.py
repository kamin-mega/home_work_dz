# 1

def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
    digits = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    str_out = digits.get(value) #"в этой переменной должен оказаться результат перевода"
    return str_out


print(num_translate("one"))
print(num_translate("eight"))
print(num_translate("Eight"))
print('-' * 50, '\n')
