from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tableDef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)

app = Flask(__name__)

#Se utilizó como base del programa el tutorial encontrado aquí https://pythonspot.com/login-authentication-with-flask/
#Se modificó para que la base de datos guardara la contraseñacon hash como medida de seguridad. El tutorial
#para hashear contraseñas se encuentra aquí https://dev.to/kaelscion/authentication-hashing-in-sqlalchemy-1bem

#La primera página adicionalmente proporcionó el template en hml y el acrhivo css para que el login no se viera horroroso

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello dude!"

@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    #query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    query = s.query(User).filter(User.username.in_([POST_USERNAME]))
    result = query.first()
    if result and result.check_password(POST_PASSWORD):
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)