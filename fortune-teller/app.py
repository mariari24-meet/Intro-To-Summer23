from flask import Flask,render_template, request, url_for, redirect
import random
app = Flask(__name__,
template_folder='templates',
static_folder='static')

@app.route('/home' , methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        birth = request.form['birthmonth']
        print(birth)
        return redirect(url_for('fortune', b = birth))

@app.route('/fortune/<b>',methods=['GET', 'POST'])
def fortune(b):
    possible_food = ["pasta", "rice", "nothing", "left overs", "pizza", "ice cream", "burgers", "eaten steak", "bad meat", "your mom's food"]
    random_item = random.choice(possible_food)
    lenth = len(b)
    if lenth > 10:
        food = "your birtday arent deffind"
    else:
        food = possible_food[lenth]

    return render_template("fortune.html", item= random_item, food2 = food)

@app.route('/' , methods=['GET' , 'POST'])
def name() :
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['name']
        month = request.form['birthmonth']
        return redirect(url_for('home', n = name , m = month))

   


    





if __name__ == '__main__':
    app.run(debug = True)

