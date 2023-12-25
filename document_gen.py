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

def create_document(course_code, course_name, specialty_code, specialty_name, qualification, approval_year, semesters, total_hours):
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
        'semesters': semesters,
        'total_hours': total_hours,
        'day': day,
        'month': month,
        'year': year
    }

    tpl.render(context)
    
    # Генерация уникального имени файла и сохранение его во временной директории
    with NamedTemporaryFile(delete=False, suffix='.docx', dir='/tmp') as tmp:
        tpl.save(tmp.name)
        unique_filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{course_code}_{course_name}.docx".replace(" ", "_")
        # Возвращаем путь к временному файлу вместо имени файла
        return tmp.name, unique_filename