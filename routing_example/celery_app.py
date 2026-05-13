from celery import Celery

app = Celery("tareas", broker="redis://localhost:6379/0",
             backend="redis://localhost:6379/0",
             task_serializer="json",
             result_serializer="json",
             imports=["tareas"],
             )