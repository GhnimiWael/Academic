import telnetlib
import time

def configure_device(HOST, PORT, networks):
    tn = telnetlib.Telnet(HOST, PORT)
    tn.write("conf t \r\n")

    # Config
    tn.write("router ospf 1 \r\n")
    for network in networks:
        tn.write("network {0} area 0 \r\n".format(network))

    # Close 
    tn.write("exit \r\n")
    tn.write("exit \r\n")
    #tn.write("exit \r\n")

    # Time to sleep for 3 seconds
    time.sleep(3)


# Configure PE1
configure_device("127.0.0.1", "5002", ["10.1.1.0 0.0.0.3", "10.1.1.4 0.0.0.3", "1.1.1.1 0.0.0.0"])

# Configure PE2
configure_device("127.0.0.1", "5004", ["10.1.1.8 0.0.0.3", "10.1.1.12 0.0.0.3", "2.2.2.2 0.0.0.0"])

# Configure P1
configure_device("127.0.0.1", "5003", ["10.1.1.20 0.0.0.3", "3.3.3.3 0.0.0.0"])

# Configure P2
configure_device("127.0.0.1", "5007", ["4.4.4.4 0.0.0.0"])
