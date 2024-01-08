from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class DocumentForm(FlaskForm):
    course_code = StringField('Код учебной дисциплины', validators=[DataRequired()])
    course_name = StringField('Название учебной дисциплины', validators=[DataRequired()])
    specialty_code = StringField('Код специальности', validators=[DataRequired()])
    specialty_name = StringField('Название специальности', validators=[DataRequired()])
    qualification = StringField('Квалификация', validators=[DataRequired()])
    approval_year = StringField('Год создания документа', validators=[DataRequired()])
    semesters = StringField('Семестры изучения', validators=[DataRequired()])
    total_hours = StringField('Общий объем часов', validators=[DataRequired()])
    course_objective = StringField('Цель освоения учебной дисциплины', validators=[DataRequired()])
    submit = SubmitField('Скачать')