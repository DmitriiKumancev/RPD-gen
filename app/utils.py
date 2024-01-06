MONTHS = {
    1: 'Января',
    2: 'Февраля',
    3: 'Марта',
    4: 'Апреля',
    5: 'Мая',
    6: 'Июня',
    7: 'Июля',
    8: 'Августа',
    9: 'Сентября',
    10: 'Октября',
    11: 'Ноября',
    12: 'Декабря'
}

def pluralize_hours(n):
    if n % 10 == 1 and n % 100 != 11:
        return f"{n} час"
    elif n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        return f"{n} часа"
    else:
        return f"{n} часов"

def pluralize_semesters(n):
    if not isinstance(n, int):
        raise TypeError(f"Expected 'n' to be an int, got {type(n)} instead.")

    if n == 1 or (n % 10 == 1 and n % 100 != 11):
        return f"{n} семестр"
    elif 2 <= n % 10 <= 4 and (n % 100 < 12 or n % 100 > 14):
        return f"{n} семестра"
    else:
        return f"{n} семестров"
