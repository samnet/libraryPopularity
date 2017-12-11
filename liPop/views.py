import os
from flask import Flask, render_template, request,json, jsonify
import liPop.db_helper as db_helper
from pymongo import MongoClient, TEXT
# from .. import config

app = Flask(__name__)
app.config.from_object('config')

# connect to database
db_name = 'lolipop0'
collection_name = 'attempt0'
conn = MongoClient(app.config["MONGOURI"])   # viz creds are in the URI
db = conn[db_name]
coll = db[collection_name]

# To get one variable, tape app.config['MY_VARIABLE']
print(app.config['MY_VARIABLE'])

@app.route('/')
def signUp():
    return render_template('UI.html')

@app.route('/sendMeDatJS', methods = [ 'GET' ])
def sendItDatJS():
    currentSelection = request.args.get("currentSelection").split(',')
    out = {}
    for pack in currentSelection:
        data = db_helper.get_document(coll, pack)
        del data["_id"]  # brute force to address ObjectID not serializable
        # print("DATA: ", data)
        out[pack] = data
    return(jsonify(out))
