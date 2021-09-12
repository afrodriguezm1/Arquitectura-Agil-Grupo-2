## Ejecutar microservicio gateway
```
cd gateway
flask run
```

## Ejecutar microservicio de cita
```
cd cita/flaskr
flask run -p 5001
```

### Ejecutar celery
```
cd cita
celery -A flaskr.tareas worker
```
