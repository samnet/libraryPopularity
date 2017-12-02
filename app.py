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
aColl = client.lipopR.coll1
if(INIT):
    aColl.create_index([('tag', TEXT)], unique = True)




def establish_collection_entry(aColl, aTag):
    found = aColl.find_one({'tag': aTag})
    if str(found) == 'None': return 'None'
    return found

def retrieve_all_pack_info(packName):
    gh = data_ret.locate_github_repo("R", packName)
    so = data_ret.tag_count_SO(packName)
    gt = data_ret.relative_pop(packName)
    cran = data_ret.dwldVol_since_inception_R(packName, total = True)
    docQual = .5
    return({"github": gh, "soflw": so, "googleTrend": gt, "cran": cran, "doc": docQual})

def populate_collection(aColl, aTag, data = {}):
    if data == {}: data = retrieve_all_pack_info(aTag)
    data["tag"] = aTag
    data["creation_date"] = datetime.datetime.utcnow()
    data["update_date"] = datetime.datetime.utcnow()
    aColl.insert_one(data)   # insert
    return(establish_collection_entry(aColl, aTag))   # verify and confirm

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

# @app.route('/sendMeDatJS', methods = [ 'GET' ])
# def sendItDatJS():
#     currentSelection = request.args.get("currentSelection").split(',')
#     print("Data:" , currentSelection)
#     githubDat = list()
#     soDat = list()
#     gPop = list()
#     cranData = list()
#     for pack in currentSelection:
#         githubDat.append(data_ret.locate_github_repo("R", pack))
#         soDat.append(data_ret.tag_count_SO(pack))
#         gPop.append(data_ret.relative_pop(pack))
#         cranData.append(data_ret.dwldVol_since_inception_R(pack, total = True))
#     out = {"github": githubDat, "soflw": soDat, "googleTrend": gPop, "cran": cranData}
#     return(jsonify(out))

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
