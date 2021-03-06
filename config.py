import os
from flask import request
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'This is a secret shhh'

    # Related to database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mail notifiaction if error occurs
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['hermankjakobsen@gmail.com']

    # Configuration for posts
    POSTS_PER_PAGE = int(os.environ.get('POSTS_PER_PAGE')) #os.environ.get('POSTS_PER_PAGE')

    # Languages supported for the app
    LANGUAGES =  os.environ.get('LANGUAGES')

    # Elasticsearch
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
