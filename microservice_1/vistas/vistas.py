from flask_restful import Resource, Api
from flask import Flask, request
import requests
import json

class VistaCitasMicro(Resource):

    def post(self):
        
        data=  request.json["nombre"]
        content = requests.post('http://127.0.0.1:5000/citas',json={'nombre': data})
        if content.status_code == 404:
            return content.json(),404
        else:
            cita = content.json()
            # registrar_puntaje.apply_async(args)
            return json.dumps(cita)

    def get(self):
        content = requests.get('http://127.0.0.1:5000/citas')
        print(content.status_code)
        if content.status_code == 404:
            return content.json(),404
        else:
            cita = content.json()
            # registrar_puntaje.apply_async(args)
            return json.dumps(cita)


