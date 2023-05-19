from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField, SelectField, RadioField, FileField, FloatField, TextAreaField
from markupsafe import Markup
from wtforms.validators import InputRequired, Regexp, Email
from wtforms.fields import EmailField
from flask_wtf.file import FileField, FileAllowed, FileRequired

class Login(FlaskForm):
    username_value = Markup('<span class="input-group-text" id="basic-addon1"><i class="fas fa-user-tie p-2"></i>Usuario</span>')
    username = StringField(username_value,validators = [InputRequired(message='Campo obligatorio'),validators.Regexp('\w+', flags=0, message='caracteres no permitidos')])
    password_value = Markup('<span class="input-group-text" id="basic-addon1"><i class="fas fa-key p-2"></i>Contraseña</span>')
    password = PasswordField(password_value, validators = [InputRequired(message='Campo obligatorio')])
    nombres_value = Markup('<span class="input-group-text" id="basic-addon1"><i class="fas fa-user p-2"></i>Nombre</span>')
    nombres = StringField(nombres_value, validators=[InputRequired(message='Campo obligatorio'), Regexp('\w+', flags=0, message='caracteres no permitidos')])
    email_value = Markup('<span class="input-group-text" id="basic-addon1"><i class="fas fa-envelope p-2"></i>Email</span>')
    email = StringField(email_value, validators=[InputRequired(message='Campo obligatorio'), Email(message='Correo electrónico inválido')])
    ingresar = SubmitField('Ingresar')
    crear = SubmitField('Crear')