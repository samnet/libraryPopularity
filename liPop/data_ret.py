'''
Goal: retrieve information about a R package, from the following sources:
- GitHub (info on popularity, description ...) - GH
- StackOverflow (info on popularity) - SO
- Google Trend (unofficial API) (same) - GT
- Cran (info on downloads over time) - Cran
Use retrieve_all_pack_info(.). It combines all the other functions specified here.

Functions defined in this module:
- retrieve_all_pack_info (combines all the below functions)
- inception_date_R (Cran)
- dwldVol_since_inception_R (CRAN)
- locate_github_repo (GH)
- tag_count_SO (SO)
- relative_pop (GT)
- historical_pop (GT)
'''

import urllib.request, json, codecs, datetime
from pytrends.request import TrendReq # google trends
import zlib

# combine info from all above mentionned sources - return a dict
def retrieve_all_pack_info(packName):
    gh = locate_github_repo("R", packName)
    so = tag_count_SO(packName)
    gt = relative_pop(packName)
    cran = dwldVol_since_inception_R(packName)
    docQual = .5
    categories = list()
    categories.append(0)
    return({"github": gh, "soflw": so, "googleTrend": gt, "cran": cran,
        "doc": docQual, "cat": categories})

## CRAN DOWNLOAD DATA

# Input:
# pack = "ggplot2"    # dbg
# pack2 = "waffect"   # dbg

# Libraries
reader = codecs.getreader("utf-8")

# Inception Date - return a string
def inception_date_R(aPackage):
    all = urllib.request.urlopen("http://crandb.r-pkg.org/" + aPackage + "/all")
    obj = json.load(reader(all))
    timeline = obj["timeline"]
    keys = list(timeline.keys())
    inception_date = timeline[keys[0]]
    return(inception_date[0:10])

# Download volume since inception date - return dict or int (sum total) if total = True
def dwldVol_since_inception_R(aPackage, total = False):
    inception_date = inception_date_R(aPackage)
    today = datetime.datetime.today()
    url = "https://cranlogs.r-pkg.org/downloads/daily/" + inception_date + ":"
    url = url + str(today)[0:10] + "/" + aPackage
    ts = urllib.request.urlopen(url)
    out = json.loads(ts.read())[0]
    if total: # compute total number of downloads since inception
        totalsum = 0
        for jour in out["downloads"]:
            totalsum = totalsum + jour["downloads"]
        return(totalsum)
    return(out)

# dwldVol_since_inception_R("ggplot2")

## LOCATING A GITHUB REPO + INFO ABOUT IT
# aPackage = "waffect  # dbg
# aLanguage = "R"      # dbg

# return dict containing all sorts of info abt package found on GH
def locate_github_repo(aLanguage, aPackage):
    url = "https://api.github.com/search/repositories?q=" + aPackage
    url = url + "+language:" + aLanguage + "&sort=stars&order=desc"
    res = urllib.request.urlopen(url)
    obj = json.load(reader(res))
    out = list()
    if obj["total_count"] == 0: return(out)   # no corresponding github repo found
    first_match = obj["items"][0]
    out.append(first_match["html_url"])   # address
    out.append(first_match["stargazers_count"]) # stars
    out.append(first_match["forks_count"]) # forks count
    out.append(first_match["updated_at"][0:10])  # last update
    out.append(first_match["description"]) # description
    return(out)

# locate_github_repo(aLanguage, packname)   # dbg

## RETRIEVING STACKOVERFLOW ACTIVITY INFO

# tag = "ggplot2"    # dbg

# retrieve no. of questions having the input as a tag - return an int
def tag_count_SO(tag):
    url = "https://api.stackexchange.com/2.2/tags/" + tag + "/"
    url = url + "related?page=1&pagesize=1&site=stackoverflow"
    soInfo = urllib.request.urlopen(url)  # this is compressed
    decompressed_data=zlib.decompress(soInfo.read(), 16+zlib.MAX_WBITS)
    jsonResponse = json.loads(decompressed_data.decode('utf-8'))
    if jsonResponse["items"] == []: return(0)  # no match on St Ov for input tag
    return(jsonResponse["items"][0]["count"])

# tag_count_SO(tag)

## GOOGLE ANALYTICS

# aPackage = "lubridate"
# aReference = "ggplot2"
# category = 0

# To do: calibrate the normalisation
# retrieve popularity (over last month) as a search concept from google trend - return an int
# nota bene: level is not informative per se.. so I normalise it wrt a  "reference"... problem:
# 1. program will bug when the reference is chosen as an input
# 2. is this normalisation meaningful?
def relative_pop(aPackage, aReference = "ggplot2", category = 0):
    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list = [aReference, aPackage]
    pytrends.build_payload(kw_list, cat = category, timeframe='today 1-m', geo='', gprop='')
    r = pytrends.interest_over_time()
    r.columns = ["Reference", "Target", "isPartial"]
    return(r['Target'].sum()/r['Reference'].sum())

# retrieve popularity as a search concept over the last 5 y
def historical_pop(kw_list):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(kw_list, cat = category, timeframe='today 5-y', geo='', gprop='')
    return(pytrends.interest_over_time())


##  RETRIEVING NO OF INCLUSIONS ON GITHUB PUBLISHED CODE
## I.E., SCRAPING GITHUB
# Not done. Is it a good idea?
# https://www.google.ch/search?q=scan+github+for+a+keyword&oq=scan+github+for+a+keyword&aqs=chrome..69i57.6424j0j7&sourceid=chrome&ie=UTF-8
