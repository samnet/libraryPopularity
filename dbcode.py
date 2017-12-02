from pymongo import MongoClient, TEXT
import datatime
client = MongoClient()


##############################################
INIT = False
# initial specification of the db

# Client - database - collection - document
client.database_names()
db.collection_names()

if(INIT):
    aDB.create_index([('tag', TEXT)], unique = True)




###############################################
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
