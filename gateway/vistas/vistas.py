import time
from celery import Celery
from flask_restful import Resource, Api
from flask import Flask, request
import requests
import json

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task(name="tabla.agendar_cita")
def agendar_cita(cita_json):
    pass


class VistaCitasMicro(Resource):

    def post(self):
        json = request.json
        json['fecha_creacion'] = str(int(time.time()))
        args = (json,)
        agendar_cita.apply_async(args)
        return "La cita esta en proceso de agendamiento", 200

    def get(self):
        try:
            content = requests.get('http://127.0.0.1:5002/citas')
        except:
            return 'Microservicio citas fallando', 404

        cita = content.json()
        return json.dumps(cita)
