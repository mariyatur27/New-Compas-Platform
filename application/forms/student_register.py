from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, IntegerField, PasswordField
from wtforms.validators import DataRequired, InputRequired


class StudentRegister(FlaskForm):
    student_name = StringField('What is your name?', validators=[DataRequired()])
    parent_name = StringField('What is your name?', validators=[DataRequired()])
    parent_email = EmailField("parent_Email", validators=[InputRequired("Please enter your email address.")])
    student_email = EmailField("student_Email", validators=[InputRequired("Please enter your email address.")])
    parent_number = IntegerField("phone", validators=[DataRequired()])
    student_grade = IntegerField("grade", validators=[DataRequired()])
    student_school = StringField('school', validators=[DataRequired()])
    student_timezone = StringField('timezone', validators=[DataRequired()])
    username = StringField("user", validators=[DataRequired()])
    password = PasswordField('pass', validators=[DataRequired()])
