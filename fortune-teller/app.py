from flask import Flask,render_template
import random
app = Flask(__name__,
template_folder='templates',
static_folder='static')


@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/fortune')
def fortune():
    possible_food = ["pasta", "rice", "nothing", "left overs", "pizza", "ice cream", "burgers", "eaten steak", "bad meat", "your mom's food"]
    random_item = random.choice(possible_food)

    return render_template("fortune.html", item= random_item)







if __name__ == '__main__':
    app.run(debug = True)

