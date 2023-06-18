from platform import system
from platform import processor
from platform import machine
import os #or this "from platform import machine.uname"
from os import getpid
import psutil

print(system())
print(processor())
print(machine())
print(os.uname())

print(getpid())

pids = getpid()
print("psutil.pids() = ", pids)
for proc in psutil.process_iter():
    try:
        pfinfo = proc.as_dict(attrs=['pid', 'name'])
    except psutil.NoSuchProcess:
        pass
    else:
        print(pfinfo)

import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

