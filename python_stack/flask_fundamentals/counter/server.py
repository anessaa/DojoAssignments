from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = 'aaa'


def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1

  

@app.route('/')
def index():
  sumSessionCounter()
  session['counter']
  return render_template("index.html")

@app.route('/button', methods=['POST'])
def pushTwo():
  sumSessionCounter()
  session['counter'] += 1
  return render_template("index.html")

@app.route('/reset', methods=['POST'])
def pushThree():
  sumSessionCounter()
  session['counter'] = 0
  return render_template("index.html")


app.run(debug=True)