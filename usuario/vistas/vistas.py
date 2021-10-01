from flask import request
from ..modelos import db, Cita, CitaSchema, Usuario, UsuarioSchema
from flask_restful import Resource
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

cita_schema = CitaSchema()
usuario_schema = UsuarioSchema()


class VistaCitas(Resource):

    def get(self):
        return [cita_schema.dump(ca) for ca in Cita.query.all()], 200


class VistaSignIn(Resource):

    def post(self):
        nuevo_usuario = Usuario(nombre=request.json["nombre"],
                                contrasena=request.json["contrasena"],
                                apellido=request.json["apellido"],
                                documento_identidad=request.json["documento_identidad"],
                                direccion=request.json["direccion"],
                                fecha_nacimiento=request.json["fecha_nacimiento"],
                                celular=request.json["celular"],
                                rol="CLIENTE")
        db.session.add(nuevo_usuario)
        db.session.commit()
        return '', 204

    def get(self):
        usuario = Usuario.query.filter(
            Usuario.documento_identidad == request.json["documento_identidad"], Usuario.contrasena == request.json["contrasena"]).first()
        db.session.commit()
        if usuario is None:
            return 'El usuario no existe', 404
        else:
            return 'Inicio de sesión exitoso', 204

class VistaSignInMedico(Resource):
    
    def post(self):
        nuevo_usuario = Usuario(nombre=request.json["nombre"],
                                contrasena=request.json["contrasena"],
                                apellido=request.json["apellido"],
                                documento_identidad=request.json["documento_identidad"],
                                direccion=request.json["direccion"],
                                fecha_nacimiento=request.json["fecha_nacimiento"],
                                celular=request.json["celular"],
                                rol="MEDICO")
        db.session.add(nuevo_usuario)
        db.session.commit()
        return '', 204


class VistaUpdateData(Resource):
    
    def delete(self):
        usuario = Usuario.query.filter(
            Usuario.documento_identidad == request.json["documento_identidad"]).first()
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
        return '', 204

    def put(self):
        usuario = Usuario.query.filter(Usuario.documento_identidad == request.json["documento_identidad"]).first()
        if usuario:
            usuario.nombre=request.json["nombre"]
            usuario.apellido=request.json["apellido"]
            usuario.contrasena=request.json["contrasena"]
            usuario.direccion=request.json["direccion"]
            usuario.fecha_nacimiento=request.json["fecha_nacimiento"]
            usuario.celular=request.json["celular"]

            db.session.commit()
            return '', 200
        else:
            return '', 404

class VistaGetRol(Resource):

    def get(self):
        usuario = Usuario.query.filter(Usuario.documento_identidad == request.json["documento_identidad"]).first()
        usarioData = usuario_schema.dump(usuario)
        if usuario:
            return {"rol": usarioData["rol"]["llave"]}
        else:
            return {"message": "el usuario no existe"}, 404