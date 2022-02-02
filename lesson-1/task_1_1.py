def convert_time(duration: int) -> str:
    d = duration // 86400  # Находим количество дней. Промежуток '/' количество секунд в сутках
    h = (duration % 86400) // 3600 # аналогично только часы.
    m = (duration % 3600) // 60 # по аналогии выше
    s = duration % 60 # по аналогии выше
    if duration < 60: # используем ветвление для проверки нужных нам условий.
        return (f'{s} сек')  # В данной строке проверка и вывод секунд.
    elif (duration >= 60) and (duration <= 3600):
        return (f'{m} мин {s} сек')
    elif (duration >= 3600) and (duration <= 86400):
        return (f'{h} час {m} мин {s} сек')
    else:
        return (f'{d} дн {h} час {m} мин {s} сек')


duration = 400153
result = convert_time(duration)
print(result)