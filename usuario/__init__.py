from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from celery import Celery

#celery = Celery(__name__, broker='redis://localhost:6379/0')


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///experimento.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app