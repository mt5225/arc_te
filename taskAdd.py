from __future__ import absolute_import
from arc_te.celery import app


@app.task
def add(x, y):
    return x+y
