# These variables are in version control.
# This file contains most of the configuration variables that your app needs.
# it s read before instance/config.py, so it overwritten by it
DEBUG = True
MY_VARIABLE = 666
#
# # Database initialization
# if os.environ.get('DATABASE_URL') is None:
#     basedir = os.path.abspath(os.path.dirname(__file__))
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# else:
#     SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


# # variables that should not be in version control are in ./instance
