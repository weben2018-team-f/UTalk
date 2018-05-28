from UTalk import app



@app.route('/')
def root():
    return render_template('root.html')