from __future__ import absolute_import
from arc_te.celery import app
import spur
import spur.ssh


@app.task(bind=True)
def run(self, **kwargs):
    shell = spur.SshShell(
        hostname=kwargs['hostname'],
        port=int(kwargs['port']),
        username=kwargs['username'],
        password=kwargs['password'],
        connect_timeout=kwargs['timeout'],
        missing_host_key=spur.ssh.MissingHostKey.accept
    )
    result = {}
    with shell:
        try:
            result = shell.run(kwargs['command'].split())
        except:
            raise
        else:
            return result.output
