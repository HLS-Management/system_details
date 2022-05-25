# system_details
Module to extract and return system details 


Syetm details
- Provides feedback of the base system for a MacOS or a Linux platform

processes
- Creates a process object; if you feed it both a process name and pid you should be able to identify if that process is working

The indended use is that you should be able to query influxdb and get a list of currently expected to be active processes; confrim they are working and if they are report back usage stats.

If they are not working you should be able to then start those processes