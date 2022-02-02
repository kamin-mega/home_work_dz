# 2

def num_translate_adv(value: str) -> str:
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
    symbol_equation = digits.get(value.lower())
    if value[0].isupper():
        return symbol_equation.capitalize()
    else:
         return symbol_equation


print(num_translate_adv("One"))
print(num_translate_adv("Two"))
print(num_translate_adv("Three"))
print(num_translate_adv("Four"))
print(num_translate_adv("Five"))
print(num_translate_adv("Six"))
print(num_translate_adv("Seven"))
print(num_translate_adv("Eight"))
print(num_translate_adv("Nine"))
print('-' * 50)
print(num_translate_adv("ten"))
print(num_translate_adv("one"))
print(num_translate_adv("two"))
print(num_translate_adv("three"))
print(num_translate_adv("four"))
print(num_translate_adv("five"))
print(num_translate_adv("six"))
print(num_translate_adv("seven"))
print(num_translate_adv("eight"))
print(num_translate_adv("nine"))
print(num_translate_adv("ten"))
