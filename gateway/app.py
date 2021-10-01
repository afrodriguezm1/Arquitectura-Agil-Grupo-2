from gateway import create_app
from flask_restful import Api

from gateway.vistas.vistas import VistaUpdateData
from .vistas import VistaCitasMicro, VistaSignIn, VistaSignInMedico
from flask_jwt_extended import JWTManager

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)
api.add_resource(VistaCitasMicro, '/cita')
api.add_resource(VistaSignIn, '/signin')
api.add_resource(VistaSignInMedico, '/signInMedico')
api.add_resource(VistaUpdateData, '/usuario')

jwt = JWTManager(app)