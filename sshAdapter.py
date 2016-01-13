from __future__ import absolute_import
from arc_te.celery import app
import spur
import spur.ssh


@app.task
def run(**kwargs):
    shell = spur.SshShell(
        hostname=kwargs['hostname'],
        port=int(kwargs['port']),
        username=kwargs['username'],
        password=kwargs['password'],
        connect_timeout=kwargs['timeout'],
        missing_host_key=spur.ssh.MissingHostKey.accept
    )
    with shell:
        result = shell.run(kwargs['command'].split())
        return result.output
