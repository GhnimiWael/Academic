import telnetlib
import time

# ====== PE1 =========
HOST = "127.0.0.1" # Console IP
PORT = "5002"        # Console Port

tn = telnetlib.Telnet(HOST, PORT)
tn.write("conf t \r\n")

# Config
tn.write("router bgp 100 \r\n")
tn.write("no bgp default ipv4-unicast \r\n")
tn.write("neighbor 2.2.2.2 remote-as 100 \r\n")
tn.write("neighbor 2.2.2.2 update-source loopback 0 \r\n")
tn.write("address-family vpnv4 unicast \r\n")
tn.write("neighbor 2.2.2.2 activate \r\n")
tn.write("neighbor 2.2.2.2 send-community both \r\n")
tn.write("address-family ipv4 vrf VPN_Customer1 \r\n")
tn.write("redistribute ospf 100 vrf VPN_Customer1 \r\n")
tn.write("address-family ipv4 vrf VPN_Customer2 \r\n")
tn.write("redistribute ospf 200 vrf VPN_Customer2 \r\n")
tn.write("exit \r\n")
tn.write("exit \r\n")
tn.write("router ospf 100 vrf VPN_Customer1 \r\n")
tn.write("redistribute bgp 100 subnets \r\n")
tn.write("network 192.168.1.0 0.0.0.3 area 11 \r\n")
tn.write("router ospf 200 vrf VPN_Customer2 \r\n")
tn.write("redistribute bgp 100 subnets \r\n")
tn.write("network 192.168.1.4 0.0.0.3 area 21 \r\n")

# Close 
tn.write("exit \r\n")
tn.write("exit \r\n")
