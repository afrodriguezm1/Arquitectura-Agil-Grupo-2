  
from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task(name="registrar_postlog")
def registrar_postlog(peticion,nombre_cita, fecha):
    with open('postlog_citas.txt','a+') as file:
        file.write('{} - {} - {}\n'.format(peticion,nombre_cita, fecha))
        

@celery.task(name="registrar_getlog")
def registrar_getlog(peticion, fecha):
    with open('getlog_citas.txt','a+') as file:
        file.write('{} - {} - {}\n'.format(peticion, fecha))