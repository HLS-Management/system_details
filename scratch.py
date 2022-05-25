import src.system_details.processes as processes
import src.system_details.system_details as sysdet
import psutil
import os
from setproctitle import setproctitle, getproctitle

name = "suchTest"
setproctitle(name)

my_process = processes.process(name=name)
my_process.define()

test = processes.check_process_status(query_pid=my_process.pid, name=name)
print(test)

test.report()
