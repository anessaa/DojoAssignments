from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def myPortfolio():
    return render_template('index.html')

@app.route('/ninja')
def ninja():

    return render_template('ninja.html', name="img/tmnt.png")

@app.route('/ninja/<name>')
def ninjaTurtle(name):
    if (name == "blue"):
        name = 'img/leonardo.jpg'
    if (name == "red"):
        name = 'img/raphael.jpg'
    if (name == "orange"):
        name = 'img/michelangelo.jpg'
    if (name == "purple"):
        name = 'img/donatello.jpg'
    else:
        name = 'img/notapril.jpg'
    return render_template('ninja.html', name = name)





app.run(debug=True)