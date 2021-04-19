from flask import Flask, render_template, request,session
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import os

app = Flask(__name__)
app.secret_key=os.urandom(24)

conn = mysql.connector.connect(host="remotemysql.com", user="NckRDEPdvn", password="IdXZK0rFXm", database="NckRDEPdvn")
cursor = conn.cursor()


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/signUp')
def about():
    return render_template('signUp.html')


@app.route('/loginValidation', methods=['POST'])
def loginValidation():
    email = request.form.get('email')
    password = request.form.get('password')

    cursor.execute("""SELECT * FROM 'users' WHERE 'email' LIKE '{}' AND 'password' LIKE '{}'""".format(email, password))

    users = cursor.fetchall()

    if len(users) > 0:

        return render_template('home.html')
    else:
        return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
