from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, PasswordField, validators

class StudentRegistrationForm(FlaskForm):
    student_name = StringField(validators=[validators.InputRequired()])
    parent_name = StringField(validators=[validators.InputRequired()])
    student_email = EmailField(validators=[validators.InputRequired(), validators.Email()])
    parent_email = EmailField(validators=[validators.InputRequired(), validators.Email()])
    parent_phone_number = StringField(validators=[validators.Optional(), validators.Regexp(r"(?:\+\d{1,2})?\(?\d{3}\)?(?:-| *)?\d{3}(?:-| *)?\d{4}")])
    student_grade = IntegerField(validators=[validators.InputRequired()])
    student_school = StringField(validators=[validators.Optional()])
    student_timezone = StringField(validators=[validators.InputRequired()])
    password = PasswordField(validators=[validators.InputRequired()])
