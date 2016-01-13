from __future__ import absolute_import
from arc_te.celery import app
import spur
import spur.ssh


@app.task
def run(*args):
    hostname = args[0]
    port = args[1]
    username = args[2]
    password = args[3]
    commamd = args[4].split()
    timeout = 30000
    shell = spur.SshShell(
        hostname=hostname,
        port=int(port),
        username=username,
        password=password,
        connect_timeout=timeout,
        missing_host_key=spur.ssh.MissingHostKey.accept
    )
    with shell:
        result = shell.run(commamd)
        return result.output
