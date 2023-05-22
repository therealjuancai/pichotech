
from flask import Flask, render_template, redirect, request, flash, g
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Email, EqualTo
import sqlite3

app=Flask(__name__)

app.secret_key = "secret_password"



'''def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
        db.row_factory = sqlite3.Row
    return db
'''

class RegistrationForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login-register', methods=['GET', 'POST'])
def login_register():
    sqliteConnection = sqlite3.connect('base.db')
    cursor = sqliteConnection.cursor()
    if request.method == 'POST':
        action=request.form["action"]
        email=request.form["email"]
        password=request.form["password"]
        if action == 'Create':

            # Verificar si el usuario ya existe en la base de datos
            
            cursor.execute("SELECT * FROM User WHERE email=?;", (email,))
            user = cursor.fetchone()
            if user is not None:
                flash('El usuario ya está registrado', 'error')
            else:
                # Insertar nuevo usuario en la base de datos
                cursor.execute("INSERT INTO User (email, password) VALUES (?, ?);", (email, password))
                sqliteConnection.commit()
                flash('Registro exitoso. Por favor, inicia sesión.', 'success')

        elif action == 'Login':
            # Verificar las credenciales del usuario en la base de datos
            cursor.execute("SELECT * FROM User WHERE email=?;", (email,))
            user = cursor.fetchone()
            if user is not None and password == user[2]:
                flash('Inicio de sesión exitoso', 'success')
                return render_template('index.html', name=email)
            else:
                flash('Credenciales inválidas', 'error')

    return render_template('login.html')
@app.teardown_appcontext
def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__== '__main__':
    app.run(debug=True)