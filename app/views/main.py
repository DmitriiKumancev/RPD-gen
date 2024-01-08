from flask import Blueprint, render_template, send_file, after_this_request, flash
from ..forms.document_form import DocumentForm
from ..services.document_service import create_document
import os

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = DocumentForm()
    if form.validate_on_submit():
        try:
            # Convert form input to integers
            semesters_int = int(form.semesters.data)
            total_hours_int = int(form.total_hours.data)
        except ValueError:
            # Handle the error if the conversion fails
            flash('Пожалуйста, введите действительное число для семестров и общего объема часов.')
            return render_template('index.html', form=form)
        
        # Создание документа с параметрами из формы
        temp_file_path, unique_filename = create_document(
            form.course_code.data,
            form.course_name.data,
            form.specialty_code.data,
            form.specialty_name.data,
            form.qualification.data,
            form.approval_year.data,
            semesters_int,  # Use the converted integer
            total_hours_int,  # Use the converted integer
            form.course_objective.data  
        )

        # Удаление временного файла после отправки
        @after_this_request
        def cleanup(response):
            os.remove(temp_file_path)
            return response

        # Возвращаем файл без указания cache_timeout
        return send_file(
            temp_file_path,
            as_attachment=True,
            download_name=unique_filename
        )

    return render_template('index.html', form=form)