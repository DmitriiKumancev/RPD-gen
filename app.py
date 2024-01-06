from flask import Flask, render_template, send_file, after_this_request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from document_gen import create_document
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

class DocumentForm(FlaskForm):
    course_code = StringField('Код учебной дисциплины', validators=[DataRequired()])
    course_name = StringField('Название учебной дисциплины', validators=[DataRequired()])
    specialty_code = StringField('Код специальности', validators=[DataRequired()])
    specialty_name = StringField('Название специальности', validators=[DataRequired()])
    qualification = StringField('Квалификация', validators=[DataRequired()])
    approval_year = StringField('Год создания документа', validators=[DataRequired()])
    semesters = StringField('Семестры изучения', validators=[DataRequired()])
    total_hours = StringField('Общий объем часов', validators=[DataRequired()])
    submit = SubmitField('Скачать')

@app.route('/', methods=['GET', 'POST'])
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
            total_hours_int  # Use the converted integer
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

if __name__ == '__main__':
    app.run()