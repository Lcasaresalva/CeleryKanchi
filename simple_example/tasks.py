from celery import Celery
from time import sleep

app = Celery("tasks", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0")


# task de ejemplo para ser ejecutada por el worker
@app.task
def add(x, y):
    i = 6
    while i > 0:
        print(f"... Processing...  wait " + str(i) + " seconds, please")
        i -= 1
        sleep(1)
    return x + y


