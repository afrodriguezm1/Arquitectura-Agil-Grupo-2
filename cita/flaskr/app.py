from importlib.resources import Resource

from flask_restful import Api

from flaskr import create_app
from .modelos import db, Cita
from .vistas import VistaCitas

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCitas, '/citas')