from docxtpl import DocxTemplate
from datetime import datetime

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

def create_document(course_code, course_name, specialty_code, specialty_name, qualification, approval_year):
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
        'day': day,
        'month': month,
        'year': year
    }

    # Генерация уникального имени файла
    filename = f"{course_code}_{course_name}.docx".replace(" ", "_")
    unique_filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{filename}"
    tpl.render(context)
    tpl.save(unique_filename)
    
    return unique_filename