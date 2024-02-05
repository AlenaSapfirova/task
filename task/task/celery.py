import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task.settings')

app = Celery('task')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'print_dayly_latest_posts': {
        'task': 'api.tasks.print_posts',
        'schedule': crontab(minute=52, hour=16)
    }
}
