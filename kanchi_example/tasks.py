from celery import Celery
from time import sleep


app = Celery("tasks", broker="redis://localhost:6379/0",
             backend="redis://localhost:6379/0",
             task_serializer="json",
             result_serializer="json",
             )


# task de ejemplo que irá a la cola de prioridad ejecutado por el worker
@app.task(queue="priority")
def add(x, y):
    i = 6
    while i > 0:
        print(f"... Estoy procesando la suma, espere " + str(i) + " segundos por favor")
        i -= 1
        sleep(1)
    return x + y


# task de ejemplo para ser ejecutada por el worker
@app.task
def multi(x, y):
    i = 6
    while i > 0:
        print(f"... Estoy procesando la multiplicación, espere " + str(i) + " segundos por favor")
        i -= 1
        sleep(1)
    return x * y
