
######################        CRAN DOWNLOAD DATA         #######################

# Input:
packname = "ggplot2"

# Libraries
import urllib.request, json, codecs, datetime
reader = codecs.getreader("utf-8")

# Inception Date
all = urllib.request.urlopen("http://crandb.r-pkg.org/" + packname + "/all")
obj = json.load(reader(all))
timeline = obj["timeline"]
keys = list(timeline.keys())
inception_date = timeline[keys[0]]
inception_date = inception_date[0:10]   # output 1

# Download volume since inception date
today = datetime.datetime.today()
url = "https://cranlogs.r-pkg.org/downloads/daily/" + inception_date + ":"
url = url + str(today.year) + "-" + str(today.month) + "-" + str(today.day) + "/" + packname
ts = urllib.request.urlopen(url)     # output 2

# https://cranlogs.r-pkg.org/downloads/daily/2014-01-03:2015-02-03/ggplot2

###################  TYING A R PACKAGE WITH A GITHUB REPO  #####################

# Input:
packname = "ggplot2"
language = "R"

url = "https://api.github.com/search/repositories?q=" + packname
url = url + "+language:" + language
res = urllib.request.urlopen(url)
obj = json.load(reader(res))
obj["items"]["owner"]["url"]


# en fait toute l info de la prochine section peut etre trouvee a ce stage
###################      RETRIEVING GITHUB REPO INFO       #####################

# Input:
guy = "jasonrudolph"
repo =  "keyboard"

url = 'https://api.github.com/repos/' + guy + '/' + repo
repoInfo = urllib.request.urlopen(url)
obj = json.load(reader(repoInfo))
obj["stargazers_count"] # output 1 - number of stars
obj["updated_at"]
# obj["has_wiki"], suscribers_count ...

########      RETRIEVING NO OF INCLUSIONS ON GITHUB PUBLISHED CODE      ########
## I.E., SCRAPING GITHUB

#############      RETRIEVING STACKOVERFLOW ACTIVITY INFO       ################
import zlib

# Input:
tag = "ggplot2"

url = "https://api.stackexchange.com/2.2/tags/" + tag + "/"
url = url + "related?page=1&pagesize=1&site=stackoverflow"
soInfo = urllib.request.urlopen(url)
decompressed_data=zlib.decompress(soInfo.read(), 16+zlib.MAX_WBITS)
jsonResponse = json.loads(decompressed_data.decode('utf-8'))
count = jsonResponse["items"][0]["count"]    # output

#############                 GOOGLE ANALYTICS                  ################
target = "ggplot2"
reference = "jquery"
category = 0

from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)
kw_list = [reference, target]
pytrends.build_payload(kw_list, cat = category, timeframe='today 1-m', geo='', gprop='')
pytrends.interest_over_time()
