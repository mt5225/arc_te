from __future__ import absolute_import
from arc_te.celery import app
from datetime import timedelta
from celery.schedules import crontab


@app.task
def add():
    app.conf.update(
        CELERYBEAT_SCHEDULE={
            'every-minute': {
                'task': 'arc_te.taskAdd.add',
                'schedule': crontab(minute='*/10'),
                'args': (1, 2),
            }
        }
    )
    return
