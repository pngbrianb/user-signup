from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/welcome", methods=['POST'])
def submit():
    username = request.form['username']

    print('Welcome, ' + username + '!')

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('homepage.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

@app.route('/',methods=['post'])
def submit():
    username = request.form['username']
    password = request.form['password']
    confirm_password =  request.form['confirm_password']
    email_address = request.form['email_address']

    if len(username) < 3 or len(username) > 20 or ' ' in username or  username = '':
        error = 'User names must be between 3 and 20 characters in length, and must not contain spaces.'
    if password != confirm_password or password

app.run()
