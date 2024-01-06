from docxtpl import DocxTemplate
from datetime import datetime
from tempfile import NamedTemporaryFile
from app.utils import pluralize_hours, pluralize_semesters, MONTHS

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