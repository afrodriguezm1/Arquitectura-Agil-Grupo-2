from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Cita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    fecha_creacion = db.Column(db.String(128))
    fecha_procesado = db.Column(db.String(128))



class CitaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Cita
        load_instance = True
