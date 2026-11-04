"""test_log_entry.py

Test to check whether the LogEntry Object has been defined and coded properly
"""

__author__ = "Aamin Vhora"



from LogEntry.LogEntry import LogEntry
import os


def test_main():

    #Test Log1
    # Jun 14 15:16:01 combo sshd(pam_unix)[19939]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=218.188.2.4 


    log1 = LogEntry("Jun 14 15:16:01", "combo", "sshd(pam_unix)[19939]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=218.188.2.4 ")

    print(log1.time)
    print(log1.host)
    print(log1.msg)



    # Use standard assert statements so pytest actually verifies the attributes are correct
    assert log1.time == "Jun 14 15:16:01"
    assert log1.host == "combo"
    assert (
        log1.msg
        == "sshd(pam_unix)[19939]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=218.188.2.4 "
    )