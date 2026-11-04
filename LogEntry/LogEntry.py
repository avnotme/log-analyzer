"""LogEntry.py

Object Class that defines LogEntry objects that hold the:
    -time
    -host
    -message
"""

__author__ = "Aamin Vhora"
__status__ = "Development"


class LogEntry:


    # Constructor
    def __init__(log, time, host, msg):
        log.time = time
        log.host = host
        log. msg = msg


    #Getter Functions

    def return_time(log):
        return log.time

    
    def return_host(log):
        return log.host

    def return_msg(log):
        return log.msg



