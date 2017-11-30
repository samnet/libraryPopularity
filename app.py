import os
import pyexcel as pe
from flask import Flask,render_template, request,json, jsonify
import data_ret

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
    print("Data:" , currentSelection)
    githubDat = list()
    soDat = list()
    gPop = list()
    cranData = list()
    for pack in currentSelection:
        githubDat.append(data_ret.locate_github_repo("R", pack))
        soDat.append(data_ret.tag_count_SO(pack))
        gPop.append(data_ret.relative_pop(pack))
        cranData.append(data_ret.dwldVol_since_inception_R(pack, total = True))
    out = {"github": githubDat, "soflw": soDat, "googleTrend": gPop, "cran": cranData}
    return(jsonify(out))

@app.route('/signUpUser', methods = [ 'GET' ])
def signUpUser():
    print(request.method)
    return json.dumps({'secret': 343});

if __name__ == "__main__":
    app.run(debug = True)
