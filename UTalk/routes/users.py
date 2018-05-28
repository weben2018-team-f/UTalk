from UTalk import app
from flask import Flask,render_template

user = Flask(__name__)

@user.route('/signup')
def registration():
    return render_template('root.html')

@user.route('/login')
def login():
    pass

@user.route('/logout')
def logout():
    pass