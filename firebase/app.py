from flask import Flask,render_template, request, url_for, redirect
from flask import session as session
import pyrebase




firebaseConfig = {
  "apiKey": "AIzaSyDRjXhtQ4rMSFfiLYbRq4j2fAWyQqA0MvY",
  "authDomain": "authentication-lab-5dc05.firebaseapp.com",
  "projectId": "authentication-lab-5dc05",
  "storageBucket": "authentication-lab-5dc05.appspot.com",
  "messagingSenderId": "692129137743",
  "appId": "1:692129137743:web:87cc524988476e9658d63a", 
  'databaseURL':"https://authentication-lab-5dc05-default-rtdb.europe-west1.firebasedatabase.app"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
app = Flask(__name__, template_folder='templates', static_folder='statics')
app.config['SECRET_KEY']= 'super-secret-key'


@app.route('/signin' , methods=['GET', 'POST'])
def signin():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    try:
      session["user"] = auth.sign_in_with_email_and_password(email, password)
      session['quotes'] = []
      return redirect(url_for('home'))
    except Exception as e:
      print(e)
    return render_template("signin.html")



  return render_template('signin.html')


@app.route('/home' , methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    quote = request.form['quote']
    try:
      session['quotes'].append(quote)
      return render_template('thanks.html')
    except Exception as errors:
      print(errors)

  return render_template('home.html')


@app.route('/thanks' , methods=['GET', 'POST'])
def thanks():
  return render_template('thanks.html')



@app.route('/display' , methods=['GET', 'POST'])
def display():
  return render_template('display.html')

@app.route('/' , methods=['GET', 'POST'])
def hello():
  error = ""
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    try:
      print(email, password)
      session['user'] = auth.create_user_with_email_and_password(email, password)
      print('made create_user_with_email_and_password')
      session['quotes'] = []
      return redirect(url_for('home'))
    except Exception as error:
      print(error)
      return render_template("signup.html")
  else:
    return render_template("signup.html")

@app.route('/signup' , methods=['GET', 'POST'])
def signup():
  # error = ""
  # if request.method == 'POST':
  #   email = request.form['email']
  #   password = request.form['password']
  #   try:
  #     print(email, password)
  #     session['user'] = auth.create_user_with_email_and_password(email, password)
  #     print('made create_user_with_email_and_password')
  #     session['quotes'] = []
  #     return redirect(url_for('home'))
  #   except:
  #     error = "Authentication failed"
  #     return render_template("signup.html")
  # else:
  return render_template("signup.html")
@app.route('/signout' , methods=['GET', 'POST'])
def signout():
  session['user'] = None
  auth.current_user = None
  return redirect(url_for('signin'))

  return render_template("signup.html")


if __name__ == '__main__':
    app.run(debug = True)



  

