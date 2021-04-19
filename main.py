from sqlite3.dbapi2 import Cursor
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

@app.route("/view")  
def view():  
    con = sqlite3.connect("admin.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Admin")  
    rows = cur.fetchall()
    return render_template("view.html",rows=rows)
            

@app.route('/loginValidation',methods = ["POST","GET"])
def loginValidation():  
    msg = "msg"  
    if request.method == "POST":  
          
            username = request.form["username"]  
            password = request.form["password"]   
            con = sqlite3.connect("admin.db")  
            con.row_factory = sqlite3.Row  
            cur = con.cursor()  
            cur.execute("select * from Admin")  
            rows = cur.fetchall()
             
            for row in rows :
                print (row) 
                if (username == row["username"]) and (password == row["password"]):                      
                        msg = "Memeber successfully login" 
                else :
                        msg = "can not login"  
    return render_template("response.html", msg = msg)  
            

if __name__ == '__main__':
    app.run(debug=True)
