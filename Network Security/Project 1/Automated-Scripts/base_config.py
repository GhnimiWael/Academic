import telnetlib
import time

# Main configuration devices
def configure_device(host, port, loopback_ip, interface_configs):
    tn = telnetlib.Telnet(host, port)
    tn.write("conf t \r\n")
    
    # Configure loopback interface
    tn.write("interface Loopback 0 \r\n")   
    tn.write("ip address {0} 255.255.255.255 \r\n".format(loopback_ip))
    tn.write("no shutdown \r\n")
    
    # Configure each interface
    for interface, ip in interface_configs.items():
        tn.write("interface {0} \r\n".format(interface))
        tn.write("ip address {0} 255.255.255.252 \r\n".format(ip))
        tn.write("no shutdown \r\n")
    
    # Close connection
    tn.write("exit \r\n")
    tn.write("exit \r\n")
    #tn.write("exit \r\n")
    time.sleep(2)
# Configure devices list
"""
Added list:
    - PE1
    - PE2
    - P1
    - P2
    - CE11
    - CE21
"""
devices = [
    ("127.0.0.1", "5002", "1.1.1.1", {"g1/0": "10.1.1.1", "g2/0": "10.1.1.5", "g3/0": "192.168.1.1", "g4/0": "192.168.1.5"}),
    ("127.0.0.1", "5004", "2.2.2.2", {"g1/0": "10.1.1.9", "g2/0": "10.1.1.13", "g3/0": "192.168.1.9", "g4/0": "192.168.1.13"}),
    ("127.0.0.1", "5003", "3.3.3.3", {"g1/0": "10.1.1.21", "g2/0": "10.1.1.2", "g3/0": "10.1.1.14"}),
    ("127.0.0.1", "5007", "4.4.4.4", {"g1/0": "10.1.1.22", "g2/0": "10.1.1.10", "g3/0": "10.1.1.6"}),
    ("127.0.0.1", "5000", "172.16.11.11", {"g1/0": "192.168.1.2"}),
    ("127.0.0.1", "5005", "172.16.12.12", {"g1/0": "192.168.1.10"}),
    ("127.0.0.1", "5001", "172.16.21.21", {"g1/0": "192.168.1.6"}),
    ("127.0.0.1", "5006", "172.16.22.22", {"g1/0": "192.168.1.14"})
]

for device in devices:
    configure_device(*device)
    time.sleep(3)