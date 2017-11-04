import os
from flask import Flask,render_template, request,json

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to Python Flask!'

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/data.csv')
def csv():
    return ('name,parent')

@app.route('/signUpUser', methods=['POST', 'GET'])
def signUpUser():
    print(request.method)
    return json.dumps({'secret': 343});

if __name__=="__main__":
    app.run()
