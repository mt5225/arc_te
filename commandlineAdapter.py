from __future__ import absolute_import
from arc_te.celery import app
import subprocess


@app.task
def run(*args):
    return subprocess.check_output(args[0].split())
