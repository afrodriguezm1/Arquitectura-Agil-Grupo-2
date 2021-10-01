from ..app import db
from ..modelos import CitaSchema, Cita
from celery import Celery
from celery.signals import task_postrun
from datetime import datetime
import time

cancion_schema = CitaSchema()

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task(name="tabla.agendar_cita")
def agendar_cita(cita_json):
    now = str(int(time.time())) #datetime.now()
    cita = Cita(nombre=cita_json["nombre"], fecha_creacion=cita_json["fecha_creacion"], fecha_procesado=now)
    db.session.add(cita)
    print(cita_json["nombre"])
    db.session.commit()

@task_postrun.connect
def close_session(*args, **kwargs):
    db.session.remove()