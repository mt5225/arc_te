from __future__ import absolute_import
from arc_te.celery import app
import spur
import spur.ssh


@app.task
def run(**kwargs):
    shell = spur.SshShell(
        hostname=kwargs['hpsa_hostname'],
        port=int(kwargs['hpsa_port']),
        username=kwargs['hpsa_username'],
        password=kwargs['hpsa_password'],
        connect_timeout=kwargs['timeout'],
        missing_host_key=spur.ssh.MissingHostKey.accept
    )
    with shell:
        command = "/opsw/bin/rosh -l %s -n %s %s" % (kwargs['target_username'], kwargs['target'], kwargs['command'])
        print(command)
        result = shell.run(command.split())
        return result.output
