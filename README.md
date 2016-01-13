# arc_te
adapters and scheduler

## sshAdapter
POST http://192.168.1.157:5555/api/task/async-apply/arc_te.sshAdapter.run

```
{
    "kwargs": {
     "hostname" : "192.168.1.210",
     "username" : "root",
     "password" : "root",
     "port" : 22,
     "timeout": 300,
     "command": "uname -a"
    },
    "options": {"max_retries": 3}
}
```

##HPSAAdapter

POST  http://192.168.1.157:5555/api/task/async-apply/arc_te.HPSAAdapter.run
```
{
    "kwargs": {
     "hpsa_hostname" : "192.168.1.210",
     "hpsa_username" : "admin",
     "hpsa_password" : "opsware_admin",
     "hpsa_port" : 2222,
     "timeout": 300,
     "target": "vm001",
     "target_username": "root",
     "command": "id"
    },
    "options": {"max_retries": 3}
}
```
