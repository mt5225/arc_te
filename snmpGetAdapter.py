from __future__ import absolute_import
from arc_te.celery import app
from pysnmp.entity.rfc3413.oneliner import cmdgen


@app.task
def run(*args):
    ip = args[0]
    community = args[1]
    oidString = args[2].split('.')
    oidNumber = [int(x) for x in oidString]
    oidValue = tuple(oidNumber)
    generator = cmdgen.CommandGenerator()
    # 1 means version SNMP v2c
    comm_data = cmdgen.CommunityData('server', community, 1)
    transport = cmdgen.UdpTransportTarget((ip, 161))
    real_fun = getattr(generator, 'nextCmd')
    res = (errorIndication, errorStatus, errorIndex, varBinds)\
        = real_fun(comm_data, transport, oidValue)
    if not errorIndication is None or errorStatus is True:
        return "Error: %s %s %s %s" % res
    else:
        return "%s" % varBinds
