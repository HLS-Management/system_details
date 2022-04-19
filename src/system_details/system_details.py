import psutil
import netifaces

import platform
import socket


def byteToGB(bytes: int):
    gb = 1073741824
    gigs = round(bytes/gb, 2)
    return gigs


class cpu:
    def __init__(self, os: str, architecture: str) -> None:
        self.core_count = psutil.cpu_count(logical=False)
        self.logical_cores = psutil.cpu_count(logical=True)
        if os == 'MacOS' and architecture == 'arm64':
            self.min_frequency = 0.0
            self.max_frequency = 0.0
        else:
            self.min_frequency = psutil.cpu_freq[1]  # Unavilible in M1/ ARM MacOS versions
            self.max_frequency = psutil.cpu_freq[2]  # Unavilible in M1/ ARM MacOS versions

    def report(self):
        print(f"Physical Cores:    {self.core_count}")
        print(f"Logical Cores:     {self.logical_cores}")
        print(f"Maximum Frequency: {self.max_frequency}GHz")
        print(f"Minimum Frequency: {self.min_frequency}GHz")


class disk:
    def __init__(self, disk: str) -> None:
        self.name = disk.mountpoint
        self.total = byteToGB(psutil.disk_usage(self.name).total)
        self.used = byteToGB(psutil.disk_usage(self.name).used)
        self.remaining = byteToGB(psutil.disk_usage(self.name).free)
        self.percentage = psutil.disk_usage(self.name).percent

    def report(self):
        print(f"Disk: {self.name} | Capacity: {self.total} | Utilised: {self.percentage}%")


class system:
    def __init__(self) -> None:
        self.os = platform.uname().system
        if self.os == 'Darwin':
            self.os = "MacOS"
        if self.os == "MacOS":
            self.ver = platform.mac_ver()[0]
        self.architecture = platform.machine()
        self.processor = cpu(os=self.os, architecture=self.architecture)
        self.memory = byteToGB(psutil.virtual_memory()[0])
        self.disks = []

        self.hostname = socket.gethostname()
        if self.hostname[-6:] == ".local":
            self.hostname = self.hostname[0:-6]

        for partition in psutil.disk_partitions():
            if self.os == 'MacOS':
                if partition.mountpoint == "/" or partition.mountpoint[0:8] == '/Volumes':
                    self.disks.append(disk(partition))

    def report(self):
        print()
        print("---- SYSTEM REPORT ----")
        print()

        print("- Operating System")
        print(f"OS:      {self.os}")
        print(f"Version: {self.ver}")
        print()

        print("- Processor")
        print(f"Architecture: {self.architecture}")
        self.processor.report()
        print()

        print(f"Memory: {self.memory}")

        for partition in self.disks:
            partition.report()
        print()
        print(f"Hostname: {self.hostname}")


test = system()

test.report()

# for interface in netifaces.interfaces():
#    print(f"{interface} | {netifaces.ifaddresses(interface)}")
    # en1 = wifi
    # en0 = eth
