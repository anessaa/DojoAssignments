from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def create_user():
   name = request.form['your_name']
   location = request.form['location']
   language = request.form['language']
   comment = request.form['comment']
   x = [name, location, language, comment]
   print name + location + language + comment
   return render_template('result.html', x = x )
app.run(debug=True) 