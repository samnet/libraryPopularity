import os
import pyexcel as pe
from flask import Flask,render_template, request,json, jsonify
import data_ret
import dbcode
from pymongo import MongoClient, TEXT

client = MongoClient()

app = Flask(__name__)

@app.route('/')
def signUp():
    return render_template('UI.html')

@app.route('/datacsv', methods = [ 'GET' ])
def csv():
    sheet = pe.load("data.csv")
    return json.dumps(sheet.to_csv());

@app.route('/sendMeDatJS', methods = [ 'GET' ])
def sendItDatJS():
    currentSelection = request.args.get("currentSelection").split(',')
    out = {}
    for pack in currentSelection:
        data = dbcode.get_document(client.lipopR.coll2, pack)
        del data["_id"]  # brute force to address ObjectID not serializable
        print("DATA: ", data)
        out[pack] = data
    print("OUT: ", out)
    return(jsonify(out))

@app.route('/signUpUser', methods = [ 'GET' ])
def signUpUser():
    print(request.method)
    return json.dumps({'secret': 343});



if __name__ == "__main__":
    app.run(debug = True)
