from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField
from wtforms.validators import InputRequired, Regexp, Email

class Login(FlaskForm):
    username = StringField('Usuario', validators=[InputRequired(message='Campo obligatorio'), validators.Regexp('\w+', flags=0, message='caracteres no permitidos')])
    password = PasswordField('Contraseña', validators=[InputRequired(message='Campo obligatorio')])
    ingresar = SubmitField('Ingresar')

class SignUp(FlaskForm):
    username = StringField('Nombre', validators=[InputRequired(message='Campo obligatorio'), Regexp('\w+', flags=0, message='caracteres no permitidos')])
    email = StringField('Email', validators=[InputRequired(message='Campo obligatorio'), Email(message='Correo electrónico inválido')])
    password = PasswordField('Contraseña', validators=[InputRequired(message='Campo obligatorio')])
    crear = SubmitField('Crear')
