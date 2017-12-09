import os
import pyexcel as pe
from flask import Flask,render_template, request,json, jsonify
import data_ret


'''DB Code
'''
from pymongo import MongoClient, TEXT
import datetime
client = MongoClient()
INIT = True
aColl = client.lipopR.coll2
if(INIT):
    aColl.create_index([('tag', TEXT)], unique = True)

# querry "aColl" for info about "aTag". If not found, return "None". 
def establish_collection_entry(aColl, aTag):
    found = aColl.find_one({'tag': aTag})
    if str(found) == 'None': return 'None'
    weekly = []
    runningCount = 0
    downloads = found["cran"]["downloads"]
    for i, msrmt in enumerate(downloads): # fount # stored daily, but use weekly
        runningCount = runningCount + msrmt["downloads"]
        if i%5 ==0:
            weekly.append({"day": msrmt["day"], "downloads": runningCount})
            runningCount = 0
    found["cran"]["downloads"] = weekly
    return found

# retrieve info about "aTag" and create entry in "aColl". Return that entry.
def populate_collection(aColl, aTag, data = {}):
    if data == {}: data = data_ret.retrieve_all_pack_info(aTag)
    data["tag"] = aTag
    data["creation_date"] = datetime.datetime.utcnow()
    data["update_date"] = datetime.datetime.utcnow()
    aColl.insert_one(data)   # insert
    return(establish_collection_entry(aColl, aTag))   # verify and confirm

# get entry corresponding to "aTag" in "aColl". If not found, create it on the way.
def get_document(aColl, aTag):
    result = establish_collection_entry(aColl, aTag)
    if (result == 'None'):
        result = populate_collection(aColl, aTag)
    return(result)

'''End DB Code
'''
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

@app.route('/sendMeDatJS', methods = [ 'GET' ])
def sendItDatJS():
    currentSelection = request.args.get("currentSelection").split(',')
    out = {}
    for pack in currentSelection:
        data = get_document(aColl, pack)
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
