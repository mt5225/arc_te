from __future__ import absolute_import

from celery import Celery

app = Celery('arc_te',
             broker='amqp://',
             backend='amqp://',
             include=['arc_te.sshAdapter', 'arc_te.wsAdapter', 'arc_te.commandlineAdapter', 'arc_te.snmpGetAdapter', 'arc_te.taskAdd', 'arc_te.HPSAAdapter'])


# setting for celery engine
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERYD_CONCURRENCY=10,  # concurrency settings
    CELERY_RESULT_BACKEND='arc_te.backends:CustomMongoBackend',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERYD_TASK_TIME_LIMIT=600,  # hard timeout for task
    CELERY_MONGODB_BACKEND_SETTINGS={
        'database': 'celery',
        'taskmeta_collection': 'taskmeta_collection'
    }
)

if __name__ == '__main__':
    app.start()
