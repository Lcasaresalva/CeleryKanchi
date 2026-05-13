from celery_app import app
from time import sleep


# task de ejemplo que irá a la cola de prioridad ejecutado por el worker
@app.task(queue="priority")
def add(x, y):
    i = 6
    while i > 0:
        print(f"... Processing the sum...  wait " + str(i) + " seconds, please")
        i -= 1
        sleep(1)
    return x + y


# task de ejemplo para ser ejecutada por el worker
@app.task
def multi(x, y):
    i = 6
    while i > 0:
        print(f"... Processing multiplication...  wait " + str(i) + " seconds, please")
        i -= 1
        sleep(1)
    return x * y
