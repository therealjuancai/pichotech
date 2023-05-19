import sqlite3

from flask import Flask, render_template, request, flash
from forms import Login 
from flask import Flask, render_template, request, jsonify, redirect, session, url_for
from flask.helpers import flash, url_for
from werkzeug.utils import secure_filename
from werkzeug.wrappers import response
from wtforms.i18n import messages_path
from markupsafe import escape
from db import consult_action, consult_select
from werkzeug.security import check_password_hash, generate_password_hash

URL_DB="pichotech.db"
app =Flask(__name__)
app.secret_key = "santiagolelo12"
conn = sqlite3.connect("pichotech.db")
cursor = conn.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        query = "SELECT * FROM usuarios WHERE username = ?"
        result = consult_select(query, (username,))
        if len(result) == 1:
            user = result[0]
            stored_password = user['password']

            # Comparar la password almacenada en la base de datos con la password ingresada
            if check_password_hash(stored_password, password):
                # La password es correcta, iniciar sesión exitosamente
                return "Inicio de sesión exitoso"

        # Las credenciales son inválidas
        flash('Credenciales inválidas')

    return render_template('sign.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = Login()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        crearUsuarios(username, email, password)
        return "Usuario registrado exitosamente"

    return render_template('index.html', form=form)

@app.route('/signup', methods=['POST'])
def crearUsuarios(username, email, password):
    try:
        with sqlite3.connect(URL_DB) as connection:
            cursor = connection.cursor()
            sql = "INSERT INTO usuarios(username, password) VALUES (?, ?)"
            cursor.execute(sql, (username, password))
            connection.commit()
            flash('Usuario registrado con éxito')
    except Exception as ex:
        flash('Error al registrar el usuario: ' + str(ex))




if __name__== '__main__':
    app.run(debug=True)
conn.close()
