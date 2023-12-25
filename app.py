from flask import Flask, render_template, send_file
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from document_gen import create_document
from io import BytesIO
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

class DocumentForm(FlaskForm):
    course_code = StringField('Код учебной дисциплины', validators=[DataRequired()])
    course_name = StringField('Название учебной дисциплины', validators=[DataRequired()])
    specialty_code = StringField('Код специальности', validators=[DataRequired()])
    specialty_name = StringField('Название специальности', validators=[DataRequired()])
    qualification = StringField('Квалификация', validators=[DataRequired()])
    approval_year = StringField('Год создания документа', validators=[DataRequired()])  # Добавлено новое поле
    submit = SubmitField('Скачать')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = DocumentForm()
    if form.validate_on_submit():
        # Создание документа с параметрами из формы
        filename = create_document(
            form.course_code.data,
            form.course_name.data,
            form.specialty_code.data,
            form.specialty_name.data,
            form.qualification.data,
            form.approval_year.data
        )
        # Чтение созданного файла для отправки пользователю
        with open(filename, 'rb') as f:
            data = f.read()
        os.remove(filename)  # Удаление файла после чтения, чтобы не хранить его на сервере
        
        # Исправление ошибки: замена `attachment_filename` на `download_name`
        return send_file(BytesIO(data), download_name=filename, as_attachment=True)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()