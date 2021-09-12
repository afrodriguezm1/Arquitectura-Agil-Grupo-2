from flask import request
from ..modelos import db, Cita, CitaSchema
from flask_restful import Resource

cita_schema = CitaSchema()
    

class VistaCitas(Resource):

    def get(self):
        return [cita_schema.dump(ca) for ca in Cita.query.all()], 200


