import os

DEBUG = False
SECRET_KEY = 'PanxuPanxu7671$'

#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:PanxuPanxu7671$@localhost/catalog_db'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_DATABASE_MODIFICATIONS = False 