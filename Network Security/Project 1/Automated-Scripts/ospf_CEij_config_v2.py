import telnetlib
import time

configurations = [
    {
        "host": "127.0.0.1",
        "port": "5000",
        "loopback_ip": "172.16.11.11",
        "g1_0_ip": "192.168.1.1",
        "ospf_area": "11"
    },
    {
        "host": "127.0.0.1",
        "port": "5005",
        "loopback_ip": "172.16.12.12",
        "g1_0_ip": "192.168.1.9",
        "ospf_area": "12"
    },
    {
        "host": "127.0.0.1",
        "port": "5001",
        "loopback_ip": "172.16.21.21",
        "g1_0_ip": "192.168.1.5",
        "ospf_area": "21"
    },
    {
        "host": "127.0.0.1",
        "port": "5006",
        "loopback_ip": "172.16.22.22",
        "g1_0_ip": "192.168.1.13",
        "ospf_area": "22"
    }
]

conf_local = "192.168.1.0"

for config in configurations:
    tn = telnetlib.Telnet(config["host"], config["port"])
    tn.write("conf t \r\n")

    # Conf
    tn.write("interface Loopback 0 \r\n")
    tn.write("ip address {0} 255.255.255.255 \r\n".format(config['loopback_ip']))
    tn.write("interface g1/0 \r\n")
    tn.write("ip address {} 255.255.255.252 \r\n".format(config['g1_0_ip']))
    tn.write("no shutdown \r\n")

    # back to conf t
    tn.write("exit\r\n")

    # ospf
    tn.write("router ospf 1 \r\n")
    tn.write("network {0} 0.0.0.3 area {1} \r\n".format(conf_local,config['ospf_area']))
    tn.write("network {0} 0.0.0.0 area {1} \r\n".format(config['loopback_ip'],config['ospf_area']))

    # Close 
    tn.write("exit \r\n")
    tn.write("exit \r\n")
    #tn.write("exit \r\n")

    # Time to sleep fo 3 seconds heheh
    time.sleep(3)
