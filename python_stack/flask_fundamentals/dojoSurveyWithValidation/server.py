from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "secretz"

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['email'])< 1:
        flash("Name cannot be empty")
        return redirect('/')
    elif len(request.form['comment']) < 1:
        flash("Comment can not be empty")
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash("Comment must be less than 120 characters!")
        return redirect('/')
    else:
        name = request.form['your_name']
        location = request.form['location']
        language = request.form['language']
        comment = request.form['comment']
        x = [name, location, language, comment]
        print x
        return render_template('/result.html', x = x )
app.run(debug=True)
