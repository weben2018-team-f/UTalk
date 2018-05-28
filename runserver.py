from UTalk import app


def main():
    #Flaskの起動
    app.run(debug=True,host='0.0.0.0')
    
if __name__ == '__main__':
    main()