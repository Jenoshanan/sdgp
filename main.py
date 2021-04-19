from flask import Flask, render_template, request,session
import os
from flask import *  
import sqlite3  


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/signUp')
def about():
    return render_template('signUp.html')

   
@app.route('/adduser',methods = ["POST","GET"])
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            username = request.form["username"]  
            email = request.form["email"]  
            password = request.form["password"]   
            with sqlite3.connect("admin.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Admin (username, email, password) values (?,?,?)",(username, email, password))  
                con.commit()  
                msg = "Memeber successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
        finally:  
            return render_template("response.html", msg = msg)  
            con.close()

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
