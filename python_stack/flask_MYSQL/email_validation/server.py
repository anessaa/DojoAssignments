from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "secretz"
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    print request.form['email']
    query = "INSERT INTO friends (email) VALUES (:email)"
    data = {
             'email': request.form['email']
           }
    mysql.query_db(query, data)
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('/success.html', all_friends=friends)


app.run(debug=True)
