import os
from flask import Flask, render_template, request,json, jsonify
import liPop.db_helper as db_helper
from pymongo import MongoClient, TEXT

# import config
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config') # fetches pkg config
app.config.from_pyfile("config.py", silent=True) # fetches instance config if available

# connect to database
db_name = app.config["DBNAME"]
collection_name = 'attempt0'
conn = MongoClient(app.config["MONGOURI"])   # viz creds are in the URI
db = conn[db_name]
coll = db[collection_name]

@app.route('/')
def signUp():
    return render_template('index.html')

@app.route('/sendMeDatJS', methods = [ 'GET' ])
def sendItDatJS():
    currentSelection = request.args.get("currentSelection").split(',')
    out = {}
    for pack in currentSelection:
        data = db_helper.get_document(coll, pack)
        del data["_id"]  # brute force to address ObjectID not serializable
        out[pack] = data
    return(jsonify(out))
