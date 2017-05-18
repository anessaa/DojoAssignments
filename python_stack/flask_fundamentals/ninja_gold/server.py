from flask import Flask, render_template, session, request, redirect
import random 
app = Flask(__name__)
app.secret_key = 'aaa'

@app.route('/')
def index():
    session['activity'] = []
    session['gold'] = 0
    return render_template("index.html")

@app.route('/process_money', methods=["POST"])
def processing():
    
    if request.form['building'] == "farm":
        newGold = random.randrange(10,20)
        session['gold'] += newGold
        session['activity'].insert(0, ('green', "Earned "+ str(newGold) + " from the farm"))
    if request.form['building'] == "cave":
        newGold = random.randrange(5,10)
        session['gold'] += newGold
        session['activity'].insert(0,('green', "Earned "+ str(newGold) + " from the cave "))
    if request.form['building'] == "house":
        newGold = random.randrange(2,5)
        session['gold'] += newGold
        session['activity'].insert(0, ('green', "Earned "+ str(newGold) + " from the house"))
    if request.form['building'] == "casino":
        newGold = random.randrange(-50, 50)
        session['gold'] += newGold
        if newGold < 0:
            session['activity'].insert(0, ('red', "Entered a casino and lost "+ str(newGold) + " ..OUCH!"))
        else:
            session['activity'].insert(0, ('green',"Earned "+ str(newGold) + " from the casino"))

    # if request.form['building'] == "casino":
    #     newGold = random.randrange(0,50)
    #     session['gold'] += newGold
    return render_template('index.html')

app.run(debug=True)