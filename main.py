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
    
    return render_template("homepage.html")


@app.route('/validate', methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    confirm_password =  request.form['confirm_password']
    email_address = request.form['email_address']

    error1 = ''
    error2 = ''
    error3 = ''
    error4 = ''

    if not username:
        error1 = 'Please enter a username.'
    elif len(username) < 3 or len(username) > 20:
        error1 = 'User names must be between 3 and 20 characters in length.'
    elif ' ' in username or '   ' in username:
        error1 = 'User names cannot contain spaces.'
        
    if not password:
        error2 = 'Please enter a password.'
    elif len(password) <3 or len(password) >20:
        error2 = 'Passwords must be between 3 and 20 characters in length.'
    elif ' ' in password or '   ' in password:
        error2 = 'Passwords cannot contain spaces.'

    if confirm_password != password:
        error3 = 'Your passwords must match.'

    if email_address and ('@' not in email_address and '.' not in email_address):
        error4 = 'An email address must contain "@" and "." (abc@123.com).'
    elif email_address and (' ' in email_address or '   ' in email_address):
        error4 = 'Email addresses cannot contain spaces.'
    elif email_address and (len(email_address) <3 or len(email_address) > 20):
        error4 = 'Email addresses must be between 3 and 20 characters in length.'

    if error1 or error2 or error3 or error4:
        return render_template("homepage.html", error1 = error1, error2 = error2, error3 = error3, error4 = error4)

    return redirect('/welcome?username=' + username)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username = username)

app.run()
