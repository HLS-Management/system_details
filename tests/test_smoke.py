import psutil
import os
from setproctitle import setproctitle, getproctitle

name = "suchTest"
setproctitle(name)

print(getproctitle())

my_pid = os.getpid()

test = psutil.Process(my_pid).as_dict()

for k,v in test.items():
    print(f"{k}: {v}")

while True:
    x = 1 + 1