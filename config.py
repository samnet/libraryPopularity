# These variables are in version control.
# This file contains most of the configuration variables that your app needs.
# it s read before instance/config.py, so it overwritten by it
DEBUG = True
MY_VARIABLE = 666


# DBUSER = "sl"
# DBPASSWORD = "imperial"
# DBPORT = "35866"
# DBNAME = "lolipop0"
# DBSERVER = "ds135866"
# MONGOURI = "mongodb://" + DBUSER + ":" + DBPASSWORD + "@"+ DBSERVER + ".mlab.com:" + DBPORT + "/" + DBNAME
 
DBUSER = "heroku_kkmn7mbg"
DBPASSWORD = "um3c11v432illv93k3o05tlfdv"
DBPORT = "37686"
DBNAME = "heroku_kkmn7mbg"
DBSERVER = "ds135866"
MONGOURI = "mongodb://heroku_kkmn7mbg:um3c11v432illv93k3o05tlfdv@ds137686.mlab.com:37686/heroku_kkmn7mbg"


#
# # Database initialization
# if os.environ.get('DATABASE_URL') is None:
#     basedir = os.path.abspath(os.path.dirname(__file__))
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# else:
#     SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


# # variables that should not be in version control are in ./instance
