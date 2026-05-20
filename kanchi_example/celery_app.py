from celery import Celery

app = Celery("tareas", broker="redis://localhost:6379/0",
             backend="redis://localhost:6379/0",
             task_serializer="json",
             result_serializer="json",
             imports=["tareas"],
             worker_send_task_events=True,
             task_send_sent_event=True,
             )
