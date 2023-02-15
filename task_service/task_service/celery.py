from celery import Celery, shared_task
import os
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_service.settings')
async_app = Celery('task_app')
async_app.config_from_object('django.conf:settings', namespace='CELERY')
async_app.autodiscover_tasks()

@async_app.task(bind=True)
def async_task(self):
    time.sleep(3)
    print("Hello")
    return True
