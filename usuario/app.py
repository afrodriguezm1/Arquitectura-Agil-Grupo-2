from importlib.resources import Resource

from flask_restful import Api

from usuario import create_app
from .modelos import db, Cita
from .vistas import VistaCitas, VistaUpdateData, VistaSignIn, VistaGetRol, VistaSignInMedico
from flask_jwt_extended import JWTManager

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
#api.add_resource(VistaCitas, '/citas')
api.add_resource(VistaSignIn, '/signIn')
api.add_resource(VistaSignInMedico, '/signInMedico')
api.add_resource(VistaUpdateData, '/usuario')
api.add_resource(VistaGetRol, '/rol')

jwt = JWTManager(app)