from flask import Flask, render_template, session, request, redirect
import random 
app = Flask(__name__)
app.secret_key = 'aaa'


@app.route('/')
def index():
  session['randomNum'] = session.get('randomNum',random.randrange(0, 101))
  print session['randomNum']
  return render_template("index.html")


@app.route('/number', methods=["POST"])
def guess():
  num = session['randomNum']
  guess = int(request.form['guess'])
  if guess > num:
    print "Guess too high!"
    session["phrase"] = "Guess too high!"
  elif guess < num:
    print "Guess too low!"
    session["phrase"] = "Guess too low!"
  else:
    print "You guessed right!"
    session["phrase"] = "YOU GUESSED RIGHT!"
  return redirect('/')

@app.route('/reset', methods=["POST"])
def reset():
  session.pop("phrase")
  session.pop("randomNum")
  return redirect("/")



app.run(debug=True)