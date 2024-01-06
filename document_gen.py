from docxtpl import DocxTemplate
from datetime import datetime
from tempfile import NamedTemporaryFile

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

def create_document(course_code, course_name, specialty_code, specialty_name, qualification, approval_year, semesters, total_hours):
    if not isinstance(semesters, int):
        raise TypeError(f"Expected 'semesters' to be an int, got {type(semesters)} instead.")
    if not isinstance(total_hours, int):
        raise TypeError(f"Expected 'total_hours' to be an int, got {type(total_hours)} instead.")

    tpl = DocxTemplate('template.docx')
    current_date = datetime.now()
    day = current_date.day
    month = MONTHS[current_date.month]
    year = current_date.year
    
    context = {
        'course_code': course_code,
        'course_name': course_name,
        'specialty_code': specialty_code,
        'specialty_name': specialty_name,
        'qualification': qualification,
        'approval_year': approval_year,
        'semesters': pluralize_semesters(semesters),
        'total_hours': pluralize_hours(total_hours),
        'day': day,
        'month': month,
        'year': year
    }

    tpl.render(context)

    with NamedTemporaryFile(delete=False, suffix='.docx', dir='/tmp') as tmp:
        tpl.save(tmp.name)
        unique_filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{course_code}_{course_name}.docx".replace(" ", "_")
        return tmp.name, unique_filename