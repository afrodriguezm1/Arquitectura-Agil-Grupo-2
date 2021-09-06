from flask import request
from ..modelos import db, Cita, CitaSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from datetime import datetime
# from celery import Celery

# celery = Celery(__name__, broker='redis://localhost:6379/0')

# @celery.task(name="registrar_postlog")
# def registrar_postlog(*args):
#     pass

# @celery.task(name="registrar_getlog")
# def registrar_getlog(*args):
#     pass


cita_schema = CitaSchema()
    

class VistaCitas(Resource):

    def post(self):
        print(request.json["nombre"])
        nueva_cita = Cita(nombre=request.json["nombre"])
        db.session.add(nueva_cita)
        db.session.commit()
        # args=("Peticion post",request.json["nombre"], datetime.utcnow())
        # registrar_postlog.apply_async(args=args, queue='postLogs')
        return cita_schema.dump(nueva_cita)

    def get(self):
        # args=("Peticion get", datetime.utcnow())
        # registrar_getlog.delay(args=args, queue='getLogs')
        return [cita_schema.dump(ca) for ca in Cita.query.all()]


