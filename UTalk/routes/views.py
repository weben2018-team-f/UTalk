from UTalk import app
from flask import Flask,render_template


@app.route('/')
def root():
    return render_template('root.html')