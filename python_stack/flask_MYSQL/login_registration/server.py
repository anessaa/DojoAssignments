from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from hashlib import md5
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "secretz"
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/register')
def register():
    return render_template('registration_form.html')
@app.route('/registration_complete')
def reg_complete():
    return render_template('/registration_complete.html')
@app.route('/success_login')
def sucess():

    return render_template('/success_login.html')


@app.route('/login', methods=['POST'])
def login():
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    email = request.form['email']
    
    query = "SELECT * FROM friends where friends.email = :email"
    data = { 'email': email
           }
    users = mysql.query_db(query, data)
    print users
    if users:
        found_user = users[0]
        if found_user['password'] == md5(request.form['password']).hexdigest():
            return redirect('/success_login')
    else:
        flash("Not a registered email")
        return redirect('/register')

@app.route('/registration_form', methods = ['POST'])
def registration():
    errors = []
    if not EMAIL_REGEX.match(request.form['email']):
        errors.append("Invalid Email Address!")
    if len(request.form['first_name']) < 2:
        errors.append("First name should at least be two characters.")
    if not request.form['first_name'].isalpha():
        errors.append("First name should be letters")
    if len(request.form['last_name']) < 2:
        errors.append("Last name should at least be two characters.")
    if not request.form['last_name'].isalpha():
        errors.append("Last name should be letters")
    if len(request.form['password']) < 8:
        errors.append("Password must be more than 8 characters")
    if not request.form['password'] == request.form['confirm_password']:
        errors.append("Password and confirmation password do not match")
    if len(errors) > 0:
        for error in errors:
            flash(error)
            return redirect('/register')
    else:
        query = "INSERT INTO friends(first_name, last_name, email, password, created_at) VALUES(:first_name, :last_name, :email, :password, NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': md5(request.form['password']).hexdigest()
               }
    mysql.query_db(query, data)
    return redirect('/registration_complete')







app.run(debug=True)
