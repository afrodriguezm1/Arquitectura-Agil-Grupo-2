from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class Cita(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(128))

class CitaSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Cita
         load_instance = True
