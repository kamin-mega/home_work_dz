import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    # пишите реализацию своей программы здесь
    indx = 0
    list_joke = []
    list_out = []
    while indx < count:
        joke = random.choice(nouns), random.choice(adverbs), random.choice(adjectives)
        list_joke.append(joke)
        for element in list_joke:
            list_out.append(list(element))
        indx += 1
    #list_out = joke #["здесь собранные шутки"]
    return list_out


print(get_jokes(2))
print(get_jokes(10))
