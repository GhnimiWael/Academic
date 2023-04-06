import telnetlib
import time

# Only PE1 and PE2
devices = [
    {"host": "127.0.0.1", "port": "5002"},
    {"host": "127.0.0.1", "port": "5004"},
]

for device in devices:
    tn = telnetlib.Telnet(device["host"], device["port"])
    tn.write("conf t \r\n")

    # Config
    tn.write("ip vrf VPN_Customer1 \r\n")
    tn.write("rd 100:1 \r\n")
    tn.write("route-target both 100:1 \r\n")
    
    tn.write("ip vrf VPN_Customer2 \r\n")
    tn.write("rd 100:2 \r\n")
    tn.write("route-target both 100:2 \r\n")

    # Return to conf-t
    tn.write("exit \r\n")

    # Activition
    tn.write("interface g3/0 \r\n")
    tn.write("ip vrf forwarding VPN_Customer1 \r\n")
    tn.write("ip address 192.168.1.1 255.255.255.252 \r\n")
    tn.write("no shutdown \r\n")

    # Return to conf-t
    tn.write("exit \r\n")

    tn.write("interface g4/0 \r\n")
    tn.write("ip vrf forwarding VPN_Customer2 \r\n")
    tn.write("ip address 192.168.1.5 255.255.255.252 \r\n")
    tn.write("no shutdown \r\n")
    

    # Close 1Z
    tn.write("exit \r\n")
    tn.write("exit \r\n")
    #tn.write("exit \r\n")

    # Time to sleep fo 3 seconds
    time.sleep(3)
