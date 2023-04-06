import telnetlib
import time

devices = [
    {"host": "127.0.0.1", "port": "5002"},
    {"host": "127.0.0.1", "port": "5004"},
    {"host": "127.0.0.1", "port": "5003"},
    {"host": "127.0.0.1", "port": "5007"}
]

for device in devices:
    tn = telnetlib.Telnet(device["host"], device["port"])
    tn.write("conf t \r\n")

    # Config
    tn.write("ip cef \r\n")
    tn.write("mpls ip \r\n")
    tn.write("mpls label protocol ldp \r\n")
    tn.write("mpls ldp router-id loopback 0 force \r\n")
    tn.write("interface g 1/0 \r\n")
    tn.write("mpls ip \r\n")
    tn.write("interface g 2/0 \r\n")
    tn.write("mpls ip \r\n")

    # Close 1Z
    tn.write("exit \r\n")
    tn.write("exit \r\n")
    #tn.write("exit \r\n")

    # Time to sleep fo 3 seconds
    time.sleep(3)
