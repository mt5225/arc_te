from __future__ import absolute_import
from arc_te.celery import app
import requests


@app.task
def run(*args):
    url = args[0]
    myResponse = requests.get(url)
    if(myResponse.ok):
        return myResponse.content
    else:
        return myResponse.raise_for_status()
