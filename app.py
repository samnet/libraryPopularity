import os
import pyexcel as pe
from flask import Flask,render_template, request,json

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to Python Flask!'

@app.route('/signUp')
def signUp():
    return render_template('UI.html')


@app.route('/datacsv', methods = [ 'GET' ])
def csv():
    sheet = pe.load("data.csv")
    return json.dumps(sheet.to_csv());


@app.route('/signUpUser', methods = [ 'GET' ])
def signUpUser():
    print(request.method)
    return json.dumps({'secret': 343});

if __name__=="__main__":
    app.run()
