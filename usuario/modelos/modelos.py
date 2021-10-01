from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
import enum

db = SQLAlchemy()

class Cita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    fecha_creacion = db.Column(db.String(128))
    fecha_procesado = db.Column(db.String(128))

class Rol(enum.Enum):
    MEDICO = 1
    CLIENTE = 2

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    apellido = db.Column(db.String(128))
    contrasena = db.Column(db.String(128))
    documento_identidad = db.Column(db.String(15))
    direccion = db.Column(db.String(128))
    fecha_nacimiento = db.Column(db.String(10)) 
    celular = db.Column(db.String(10))
    rol = db.Column(db.Enum(Rol))

class CitaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Cita
        load_instance = True

class EnumADiccionario(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {"llave": value.name, "valor": value.value}

class UsuarioSchema(SQLAlchemyAutoSchema):
    rol = EnumADiccionario(attribute=("rol"))
    class Meta:
        model = Usuario
        load_instance = True
