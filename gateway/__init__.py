from flask import Flask

def create_app(config_name):
    app = Flask(__name__)     
    app.config['JWT_SECRET_KEY']='frase-secreta'
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app