from celery import Celery
from datetime import timedelta, datetime
from django.conf import settings
import os


REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ravApp.settings")

app = Celery('tasks', broker=f"redis://{REDIS_HOST}:{REDIS_PORT}")

app.conf.beat_schedule = {
    'backup-every-hour': {
        'task': 'tasks.backup_data',
        'schedule': timedelta(seconds=60*60*12) # каждые 12 часов
    },
}
app.conf.timezone = 'UTC'


@app.task
def backup_data():
    command = f"PGPASSWORD='{settings.DATABASES['default']['PASSWORD']}' pg_dump -U {settings.DATABASES['default']['USER']} -h {settings.DATABASES['default']['HOST']} -p {settings.DATABASES['default']['PORT']} -d {settings.DATABASES['default']['NAME']} > /backups/backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.sql"
    os.system(command)