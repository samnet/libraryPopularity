import os
from flask import Flask, render_template, request,json, jsonify
import liPop.db_helper as db_helper
from pymongo import MongoClient, TEXT
# from pymongo import MongoClient
# from .. import config
client = MongoClient()     # how do we access the (secret) constants of config.py?

app = Flask(__name__)

app.config.from_object('config')
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
        data = db_helper.get_document(client.lipopR.coll2, pack)
        del data["_id"]  # brute force to address ObjectID not serializable
        # print("DATA: ", data)
        out[pack] = data
    return(jsonify(out))
