from pymongo import MongoClient
client = MongoClient()

def establish_DB_entry(aTag):
    found = test.find_one({'tag': aTag})
    if str(found) == 'None': return 'None'
    return found

def retrieve_all_pack_info(packName):
    gh = data_ret.locate_github_repo("R", packName)
    so = data_ret.tag_count_SO(packName)
    gt = data_ret.relative_pop(packName)
    cran = data_ret.dwldVol_since_inception_R(packName, total = True)
    docQual = .5
    return({"github": gh, "soflw": so, "googleTrend": gt, "cran": cran, "doc": docQual})

def populateDB(aTag):
    data = retrieve_all_pack_info(aTag)
    entry = merge({"tag": aTag}, data)
    db.insert(data)

def queryDB(aTag):
    result = establish_DB_entry(aTag)
    if (result == 'None'):
        populateDB(aTag)
    return(result)
