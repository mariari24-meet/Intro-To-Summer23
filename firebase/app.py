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
  'databaseURL':""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='statics')
app.config['SECRET_KEY']= 'super-secret-key'


@app.route('/signin' , methods=['GET', 'POST'])
def signin():
  return render_template('signin.html')


@app.route('/home' , methods=['GET', 'POST'])
def home():
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
  #   return render_template("signup.html")
@app.route('/signout' , methods=['GET', 'POST'])
def signout():


if __name__ == '__main__':
    app.run(debug = True)



  

