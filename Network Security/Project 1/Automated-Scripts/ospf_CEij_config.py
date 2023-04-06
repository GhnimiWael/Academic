import telnetlib
import time

# ================== CE11 =========
HOST = "127.0.0.1" # Console IP
PORT = "5000"        # Console Port

tn = telnetlib.Telnet(HOST, PORT)
tn.write("conf t \r\n")

# Conf
tn.write("interface Loopback 0 \r\n")
tn.write("ip address 172.16.11.11 255.255.255.255 \r\n")
tn.write("interface g1/0 \r\n")
tn.write("ip address 192.168.1.1 255.255.255.252 \r\n")
tn.write("no shutdown \r\n")

# back to conf t
tn.write("exit\r\n")

# ospf
tn.write("network 192.168.1.0 0.0.0.3 area 11 \r\n")
tn.write("network 172.16.11.11 0.0.0.0 area 11 \r\n")


# Close 
tn.write("exit \r\n")
tn.write("exit \r\n")
tn.write("exit \r\n")
tn.close()

# Time to sleep fo 3 seconds heheh
time.sleep(3)

# ================== CE12 =========
HOST = "127.0.0.1" # Console IP
PORT = "5005"        # Console Port

tn = telnetlib.Telnet(HOST, PORT)
tn.write("conf t \r\n")

# Conf
tn.write("interface Loopback 0 \r\n")
tn.write("ip address 172.16.12.12 255.255.255.255 \r\n")
tn.write("interface g1/0 \r\n")
tn.write("ip address 192.168.1.9 255.255.255.252 \r\n")
tn.write("no shutdown \r\n")

# back to conf t
tn.write("exit\r\n")

# ospf
tn.write("network 192.168.1.0 0.0.0.3 area 11 \r\n")
tn.write("network 172.16.12.12 0.0.0.0 area 11 \r\n")


# Close 
tn.write("exit \r\n")
tn.write("exit \r\n")
tn.write("exit \r\n")
tn.close()

# Time to sleep fo 3 seconds heheh
time.sleep(3)

# ================== CE21 =========
HOST = "127.0.0.1" # Console IP
PORT = "5001"        # Console Port

tn = telnetlib.Telnet(HOST, PORT)
tn.write("conf t \r\n")

# Conf
tn.write("interface Loopback 0 \r\n")
tn.write("ip address 172.16.21.21 255.255.255.255 \r\n")
tn.write("interface g1/0 \r\n")
tn.write("ip address 192.168.1.5 255.255.255.252 \r\n")
tn.write("no shutdown \r\n")

# back to conf t
tn.write("exit\r\n")

# ospf
tn.write("network 192.168.1.0 0.0.0.3 area 11 \r\n")
tn.write("network 172.16.21.21 0.0.0.0 area 11 \r\n")


# Close 
tn.write("exit \r\n")
tn.write("exit \r\n")
tn.write("exit \r\n")
tn.close()

# Time to sleep fo 3 seconds heheh
time.sleep(3)

# ================== CE22 =========
HOST = "127.0.0.1" # Console IP
PORT = "5006"        # Console Port

tn = telnetlib.Telnet(HOST, PORT)
tn.write("conf t \r\n")

# Conf
tn.write("interface Loopback 0 \r\n")
tn.write("ip address 172.16.22.22 255.255.255.255 \r\n")
tn.write("interface g1/0 \r\n")
tn.write("ip address 192.168.1.13 255.255.255.252 \r\n")
tn.write("no shutdown \r\n")

# back to conf t
tn.write("exit\r\n")

# ospf
tn.write("network 192.168.1.0 0.0.0.3 area 11 \r\n")
tn.write("network 172.16.22.22 0.0.0.0 area 11 \r\n")


# Close 
tn.write("exit \r\n")
tn.write("exit \r\n")
tn.write("exit \r\n")
tn.close()

# Time to sleep fo 3 seconds heheh
time.sleep(3)



print("HERE WE GO !! STAGE CEij OSPF Completed!\nTHANK YOU FOR UR TIME BROOO <3 SEE YA ... \n")