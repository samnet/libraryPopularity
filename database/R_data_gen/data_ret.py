
######################        CRAN DOWNLOAD DATA         #######################

# Input:
packname = "abjutils"

# Libraries
import urllib.request, json, codecs, datetime
reader = codecs.getreader("utf-8")

# Inception Date
def inception_date_R(aPackage):
    all = urllib.request.urlopen("http://crandb.r-pkg.org/" + aPackage + "/all")
    obj = json.load(reader(all))
    timeline = obj["timeline"]
    keys = list(timeline.keys())
    inception_date = timeline[keys[0]]
    return(inception_date[0:10])

# Download volume since inception date
def dwldVol_since_inception_R(aPackage):
    inception_date = inception_date_R(aPackage)
    today = datetime.datetime.today()
    url = "https://cranlogs.r-pkg.org/downloads/daily/" + inception_date + ":"
    url = url + str(today.year) + "-" + str(today.month) + "-" + str(today.day) + "/" + packname
    ts = urllib.request.urlopen(url)
    return(ts.read())

# https://cranlogs.r-pkg.org/downloads/daily/2014-01-03:2015-02-03/ggplot2

###################  LOCATING A GITHUB REPO + INFO ON IT   #####################

# Input:
aPackage = "ggplot2"
aLanguage = "R"

def locate_github_repo(aLanguage, aPackage):
    url = "https://api.github.com/search/repositories?q=" + aPackage
    url = url + "+language:" + aLanguage + "&sort=stars&order=desc"
    res = urllib.request.urlopen(url)
    obj = json.load(reader(res))
    first_match = obj["items"][0]
    out = list()
    out.append(first_match["html_url"])   # address
    out.append(first_match["stargazers_count"]) # stars
    out.append(first_match["forks_count"]) # forks count
    out.append(first_match["updated_at"][0:10])  # last update
    out.append(first_match["description"]) # description
    return(out)

locate_github_repo(language, packname)


########      RETRIEVING NO OF INCLUSIONS ON GITHUB PUBLISHED CODE      ########
## I.E., SCRAPING GITHUB

#############      RETRIEVING STACKOVERFLOW ACTIVITY INFO       ################
import zlib

# Input:
tag = "ggplot2"

def tag_count_SO(tag):
    url = "https://api.stackexchange.com/2.2/tags/" + tag + "/"
    url = url + "related?page=1&pagesize=1&site=stackoverflow"
    soInfo = urllib.request.urlopen(url)
    decompressed_data=zlib.decompress(soInfo.read(), 16+zlib.MAX_WBITS)
    jsonResponse = json.loads(decompressed_data.decode('utf-8'))
    return(jsonResponse["items"][0]["count"])    # output

tag_count_SO(tag)
#############                 GOOGLE ANALYTICS                  ################

from pytrends.request import TrendReq

target = "ggplot2"
reference = "jquery"
category = 0

def relativePop(aPackage, aReference = "jquery"):
    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list = [aReference, aPackage]
    pytrends.build_payload(kw_list, cat = category, timeframe='today 1-m', geo='', gprop='')
    r = pytrends.interest_over_time()
    r.columns = ["Reference", "Target", "isPartial"]
    return(r['Target'].sum()/r['Reference'].sum())
# should perhaps get rid of cat arg to keep default value
def historicalPop(kw_list):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(kw_list, cat = category, timeframe='today 5-y', geo='', gprop='')
    return(pytrends.interest_over_time())
