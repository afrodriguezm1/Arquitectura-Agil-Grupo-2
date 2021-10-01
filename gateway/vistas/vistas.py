import time
#from celery import Celery
from flask_restful import Resource, Api
from flask import Flask, request
import requests
import json
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

#app = Celery('tasks', broker='redis://localhost:6379/0')


#@app.task(name="tabla.agendar_cita")
#def agendar_cita(cita_json):
#    pass


class VistaCitasMicro(Resource):

    def post(self):
        json = request.json
        json['fecha_creacion'] = str(int(time.time()))
        args = (json,)
        #agendar_cita.apply_async(args)
        return "La cita esta en proceso de agendamiento", 200

    def get(self):
        try:
            content = requests.get('http://127.0.0.1:5002/citas')
        except:
            return 'Microservicio citas fallando', 404

        cita = content.json()
        return json.dumps(cita)


class VistaSignIn(Resource):

    def post(self):
        content = requests.post('http://127.0.0.1:5002/signIn', json={'nombre': request.json["nombre"],
                                'contrasena': request.json["contrasena"],
                                'apellido': request.json["apellido"],
                                'documento_identidad': request.json["documento_identidad"],
                                'direccion': request.json["direccion"],
                                'fecha_nacimiento': request.json["fecha_nacimiento"],
                                'celular': request.json["celular"] })
        if(content.status_code == 204):
            token_de_acceso = create_access_token(identity=request.json["documento_identidad"])
            return {"token de acceso": token_de_acceso}
        else:
            return {"message": "error al hacer signIn"}, 404

    def get(self):
        content = requests.get('http://127.0.0.1:5002/signIn', json={'documento_identidad': request.json["documento_identidad"],'contrasena': request.json["contrasena"]})
        if content.status_code == 204:
            token_de_acceso = create_access_token(identity=request.json["documento_identidad"])
            return {"token de acceso": token_de_acceso}
        else:
            return {"message": "error al hacer signIn"}, 404

class VistaSignInMedico(Resource):
    
    def post(self):
        content = requests.post('http://127.0.0.1:5002/signInMedico', json={'nombre': request.json["nombre"],
                                'contrasena': request.json["contrasena"],
                                'apellido': request.json["apellido"],
                                'documento_identidad': request.json["documento_identidad"],
                                'direccion': request.json["direccion"],
                                'fecha_nacimiento': request.json["fecha_nacimiento"],
                                'celular': request.json["celular"] })
        if(content.status_code == 204):
            token_de_acceso = create_access_token(identity=request.json["documento_identidad"])
            return {"token de acceso": token_de_acceso}
        else:
            return {"message": "error al hacer signIn"}, 404

class VistaUpdateData(Resource):
    
    @jwt_required()
    def delete(self):
        identity = get_jwt_identity()
        rol = requests.get('http://127.0.0.1:5002/rol', json={'documento_identidad': identity})
        if rol.status_code == 200:
            if rol.json()['rol'] == "MEDICO":
                content = requests.delete('http://127.0.0.1:5002/usuario', json={'documento_identidad': request.json["documento_identidad"]})
                if content.status_code == 204:
                    return {"message":"Usuario se eliminó exitosamente"}, 200
                else:
                    return {"message":"el usuario no está autenticado"}, 404
            else:
                return "El usuario no tiene permisos para esta acción", 404
        else:
            return "Ocurrio un erro", 404

    @jwt_required()
    def put(self):
        identity = get_jwt_identity()
        rol = requests.get('http://127.0.0.1:5002/rol', json={'documento_identidad': identity})
        if rol.status_code == 200:
            if rol.json()['rol'] == "CLIENTE":
                content = requests.put('http://127.0.0.1:5002/usuario', json={'nombre': request.json["nombre"],
                                        'contrasena': request.json["contrasena"],
                                        'apellido': request.json["apellido"],
                                        'documento_identidad': request.json["documento_identidad"],
                                        'direccion': request.json["direccion"],
                                        'fecha_nacimiento': request.json["fecha_nacimiento"],
                                        'celular': request.json["celular"] })
                if(content.status_code == 200):
                    return {"message": "el usuario se actualizó correctamente"}
                else:
                    return {"message": "error no se actualizó"}, 404
            else:
                return "El usuario no tiene permisos para esta acción", 404
        else:
            return "Ocurrio un error", 404
