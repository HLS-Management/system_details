import psutil
import platform
import socket
import os


class process:
    def __init__(self, name: str, tags: set = None) -> None:
        self.tags = tags
        self.name = name

    def define(self, pid: int = None):
        if pid is None:
            self.pid = os.getpid()
        else:
            self.pid = pid
        self.hostname = socket.gethostname()
        if self.hostname[-6:] == ".local":
            self.hostname = self.hostname[0:-6]

    def snapshot(self, cpu_percent: float, memory_percent: float, cpu_affinity: int = 0):
        self.cpu_percent = cpu_percent
        self.memory_percent = memory_percent
        self.cpu_affinity = cpu_affinity

    def report(self):
        print(f"Name:     {self.name}")
        print(f"tags:     {self.tags}")
        print(f"PID:      {self.pid}")
        print(f"Host:     {self.hostname}")
        print(f"CPU %:    {self.cpu_percent} %")
        print(f"CPU Core: {self.cpu_affinity}")
        print(f"Memory:   {self.memory_percent} %")


def check_process_status(query_pid: int, name: str) -> process:
    '''Takes in an PID and checks the status of the PID; assumes that the script is Python'''
    try:
        system_process = psutil.Process(query_pid)
        if system_process.name() != name:
            return False

        response = process(name=name)
        response.define(pid=query_pid)
        if platform.uname().system == 'Darwin':
            percent = system_process.cpu_percent()
            memory = round(system_process.memory_percent(), 2)
            affinity = 0
        if platform.uname().system == 'Linux':
            pass  # We will need to implement memory extraction logic
        response.snapshot(cpu_percent=percent, memory_percent=memory, cpu_affinity=affinity)

        return response

    except Exception as error:
        if isinstance(error, psutil.NoSuchProcess):
            return False
        else:
            return error


def kill_unexpected_processes() -> None:
    pass
