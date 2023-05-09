from flask import Flask, render_template, request
from random import randint, randrange
import datetime
import time
import sqlite3

app = Flask(__name__, template_folder= "templates")

app.config["TEMPLATES_AUTO_RELOAD"] = True

#create connection with users.db
connection = sqlite3.connect('users.db', check_same_thread=False)

#create table called user
connection.execute('''CREATE TABLE IF NOT EXISTS user(
    userNum INTEGER PRIMARY KEY autoincrement,
    firstname CHAR(20) NOT NULL,
    lastname CHAR(20) NOT NULL,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    pin INTEGER(6),
    ssn INTEGER(9))
''')
connection.commit()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods = ['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    cursor = connection.execute("SELECT * from user WHERE username = ? and password = ?", (username, password))

    if not cursor.fetchone():
        return render_template("register.html")
    else:
        return render_template("menu.html")

        
@app.route("/", methods = ['POST'])    
def register():
    print("got here")
    '''range_start = 10**(15)
    range_end = (10**16)-1
    debitcard = randint(range_start, range_end)
    range_start = 10**(1)
    range_end = (10**16)-1'''
    username = request.form.get("username")
    password = request.form.get("password")
    '''firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    pin = request.form.get("pin")
    ssn = request.form.get("ssn")'''
    connection.execute("INSERT INTO user (username, password) VALUES(?, ?)", username, password)
    connection.commit()
    return render_template("index.html")

if __name__ == "__main__":
    app.run('localhost', 8080) 