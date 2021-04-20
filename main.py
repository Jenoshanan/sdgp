from sqlite3.dbapi2 import Cursor
from flask import Flask, render_template, request,redirect,session
import os
from flask import *  
import sqlite3  


app = Flask(__name__)
app.secret_key=os.urandom(24)

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/signUp')
def about():
    return render_template('signUp.html')

   
@app.route('/adduser',methods = ["POST","GET"])
def saveDetails():  
  
    if request.method == "POST":  
        try:  
            username = request.form["username"]  
            email = request.form["email"]  
            password = request.form["password"]   
            with sqlite3.connect("admin.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Admin (username, email, password) values (?,?,?)",(username, email, password))  
                con.commit()               
        except:  
            con.rollback()  
        finally:  
            return redirect('/')
            con.close()

@app.route('/response')
def response():  
    if 'ID' in session:
        return render_template('response.html') 
    else:    
        return redirect('/') 


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
    if request.method == "POST":  
          
            username = request.form["username"]  
            password = request.form["password"]   
            con = sqlite3.connect("admin.db")  
            con.row_factory = sqlite3.Row  
            cur = con.cursor()  
            cur.execute("select * from Admin WHERE username = ?",[username,])  
            cur.execute("select * from Admin WHERE password = ?",[password,])  
            rows = cur.fetchall()
             
            for row in rows :
                print (row) 
                if (username == row["username"]) and (password == row["password"]):                      
                        session['ID'] = rows[0][0]
                        return redirect('/response')  
                else :
                        return redirect('/')  
  
            
@app.route('/logout')
def logout():  
    session.pop('ID')
    return redirect('/') 


if __name__ == '__main__':
    app.run(debug=True)
