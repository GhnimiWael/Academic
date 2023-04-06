# Network Architecuture
<p align="center" width="100%">
    <img width="100%"src="https://i.imgur.com/W2dCJw8.png"> 
</p>
- All information asked to be completed of this project are on the "cahier de charge" document.

# Configuration de base de l'adressage de chaque interface

For that i used the following script:
```python
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
```

## Useful Commands
- *sh ip int br* - display a brief status of interfaces

## CE11
```c
CE11#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                unassigned      YES unset  administratively down down    
GigabitEthernet0/0         unassigned      YES unset  administratively down down    
GigabitEthernet1/0         192.168.1.2     YES manual up                    up      
GigabitEthernet2/0         unassigned      YES unset  administratively down down    
SSLVPN-VIF0                unassigned      NO  unset  up                    up      
Loopback0                  172.16.11.11    YES manual up                    up      
CE11#
```
## CE12
```c
CE12#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                unassigned      YES unset  administratively down down    
GigabitEthernet0/0         unassigned      YES unset  administratively down down    
GigabitEthernet1/0         192.168.1.10    YES manual up                    up      
GigabitEthernet2/0         unassigned      YES unset  administratively down down    
SSLVPN-VIF0                unassigned      NO  unset  up                    up      
Loopback0                  172.16.12.12    YES manual up                    up      
CE12#

```
## CE21
```c
CE21#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                unassigned      YES unset  administratively down down    
GigabitEthernet0/0         unassigned      YES unset  administratively down down    
GigabitEthernet1/0         192.168.1.6     YES manual up                    up      
GigabitEthernet2/0         unassigned      YES unset  administratively down down    
SSLVPN-VIF0                unassigned      NO  unset  up                    up      
Loopback0                  172.16.21.21    YES manual up                    up      
CE21#
```

## CE22
```c
CE22#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                unassigned      YES unset  administratively down down    
GigabitEthernet0/0         unassigned      YES unset  administratively down down    
GigabitEthernet1/0         192.168.1.14    YES manual up                    up      
GigabitEthernet2/0         unassigned      YES unset  administratively down down    
SSLVPN-VIF0                unassigned      NO  unset  up                    up      
Loopback0                  172.16.22.22    YES manual up                    up      
CE22#
```

## PE1
```c
PE1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                unassigned      YES NVRAM  administratively down down    
GigabitEthernet0/0         unassigned      YES NVRAM  administratively down down    
GigabitEthernet1/0         10.1.1.1        YES NVRAM  up                    up      
GigabitEthernet2/0         10.1.1.5        YES NVRAM  up                    up      
GigabitEthernet3/0         192.168.1.1     YES NVRAM  up                    up      
GigabitEthernet4/0         192.168.1.5     YES NVRAM  up                    up      
SSLVPN-VIF0                unassigned      NO  unset  up                    up      
Loopback0                  1.1.1.1         YES NVRAM  up                    up      
PE1#
```
## PE2
```c
PE2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                unassigned      YES unset  administratively down down    
GigabitEthernet0/0         unassigned      YES unset  administratively down down    
GigabitEthernet1/0         10.1.1.9        YES manual up                    up      
GigabitEthernet2/0         10.1.1.13       YES manual up                    up      
GigabitEthernet3/0         192.168.1.9     YES manual up                    up      
GigabitEthernet4/0         192.168.1.13    YES manual up                    up      
SSLVPN-VIF0                unassigned      NO  unset  up                    up      
Loopback0                  2.2.2.2         YES manual up                    up      
PE2#
```
## P1
```c
P1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                unassigned      YES unset  administratively down down    
GigabitEthernet0/0         unassigned      YES unset  administratively down down    
GigabitEthernet1/0         10.1.1.21       YES manual up                    up      
GigabitEthernet2/0         10.1.1.2        YES manual up                    up      
GigabitEthernet3/0         10.1.1.14       YES manual up                    up      
SSLVPN-VIF0                unassigned      NO  unset  up                    up      
Loopback0                  3.3.3.3         YES manual up                    up      
P1#
```

## P2
```c
P2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                unassigned      YES unset  administratively down down    
GigabitEthernet0/0         unassigned      YES unset  administratively down down    
GigabitEthernet1/0         10.1.1.22       YES manual up                    up      
GigabitEthernet2/0         10.1.1.10       YES manual up                    up      
GigabitEthernet3/0         10.1.1.6        YES manual up                    up      
SSLVPN-VIF0                unassigned      NO  unset  up                    up      
Loopback0                  4.4.4.4         YES manual up                    up      
P2#
```

# Routage OSPF de Backbone IP/MPLS
For that i used the following script:
```python
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
```
## P1
```c
P1#show ip ospf neighbor 

Neighbor ID     Pri   State           Dead Time   Address         Interface
2.2.2.2           1   FULL/DR         00:00:36    10.1.1.13       GigabitEthernet3/0
1.1.1.1           1   FULL/DR         00:00:30    10.1.1.1        GigabitEthernet2/0
4.4.4.4           1   FULL/BDR        00:00:36    10.1.1.22       GigabitEthernet1/0
P1#show ip route ospf    
     1.0.0.0/32 is subnetted, 1 subnets
O       1.1.1.1 [110/2] via 10.1.1.1, 00:18:00, GigabitEthernet2/0
     2.0.0.0/32 is subnetted, 1 subnets
O       2.2.2.2 [110/2] via 10.1.1.13, 00:13:45, GigabitEthernet3/0
     4.0.0.0/32 is subnetted, 1 subnets
O       4.4.4.4 [110/2] via 10.1.1.22, 00:05:24, GigabitEthernet1/0
     10.0.0.0/30 is subnetted, 5 subnets
O       10.1.1.8 [110/2] via 10.1.1.22, 00:05:24, GigabitEthernet1/0
                 [110/2] via 10.1.1.13, 00:13:45, GigabitEthernet3/0
O       10.1.1.4 [110/2] via 10.1.1.22, 00:05:24, GigabitEthernet1/0
                 [110/2] via 10.1.1.1, 00:18:00, GigabitEthernet2/0
P1#

```

##  P2
```c
P2#sh ip ospf neighbor 

Neighbor ID     Pri   State           Dead Time   Address         Interface
3.3.3.3           1   FULL/DR         00:00:35    10.1.1.21       GigabitEthernet1/0
2.2.2.2           1   FULL/DR         00:00:39    10.1.1.9        GigabitEthernet2/0
1.1.1.1           1   FULL/DR         00:00:32    10.1.1.5        GigabitEthernet3/0
P2#sh ip route ospf
     1.0.0.0/32 is subnetted, 1 subnets
O       1.1.1.1 [110/2] via 10.1.1.5, 00:08:38, GigabitEthernet3/0
     2.0.0.0/32 is subnetted, 1 subnets
O       2.2.2.2 [110/2] via 10.1.1.9, 00:08:22, GigabitEthernet2/0
     3.0.0.0/32 is subnetted, 1 subnets
O       3.3.3.3 [110/2] via 10.1.1.21, 00:06:33, GigabitEthernet1/0
     10.0.0.0/30 is subnetted, 5 subnets
O       10.1.1.12 [110/2] via 10.1.1.21, 00:06:33, GigabitEthernet1/0
                  [110/2] via 10.1.1.9, 00:08:22, GigabitEthernet2/0
O       10.1.1.0 [110/2] via 10.1.1.21, 00:06:33, GigabitEthernet1/0
                 [110/2] via 10.1.1.5, 00:08:38, GigabitEthernet3/0
P2#

```

## PE1
```c
PE1#show ip ospf neighbor 

Neighbor ID     Pri   State           Dead Time   Address         Interface
4.4.4.4           1   FULL/BDR        00:00:31    10.1.1.6        GigabitEthernet2/0
3.3.3.3           1   FULL/BDR        00:00:39    10.1.1.2        GigabitEthernet1/0
PE1#show ip route ospf
     2.0.0.0/32 is subnetted, 1 subnets
O       2.2.2.2 [110/3] via 10.1.1.6, 00:07:21, GigabitEthernet2/0
                [110/3] via 10.1.1.2, 00:13:54, GigabitEthernet1/0
     3.0.0.0/32 is subnetted, 1 subnets
O       3.3.3.3 [110/2] via 10.1.1.2, 00:18:18, GigabitEthernet1/0
     4.0.0.0/32 is subnetted, 1 subnets
O       4.4.4.4 [110/2] via 10.1.1.6, 00:07:48, GigabitEthernet2/0
     10.0.0.0/30 is subnetted, 5 subnets
O       10.1.1.8 [110/2] via 10.1.1.6, 00:07:21, GigabitEthernet2/0
O       10.1.1.12 [110/2] via 10.1.1.2, 00:13:54, GigabitEthernet1/0
O       10.1.1.20 [110/2] via 10.1.1.6, 00:05:42, GigabitEthernet2/0
                  [110/2] via 10.1.1.2, 00:18:18, GigabitEthernet1/0
PE1#
```

## PE2
```c
PE2#sh ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
3.3.3.3           1   FULL/BDR        00:00:36    10.1.1.14       GigabitEthernet2/0
4.4.4.4           1   FULL/BDR        00:00:35    10.1.1.10       GigabitEthernet1/0
PE2#sh ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
3.3.3.3           1   FULL/BDR        00:00:33    10.1.1.14       GigabitEthernet2/0
4.4.4.4           1   FULL/BDR        00:00:32    10.1.1.10       GigabitEthernet1/0
PE2#show ip route ospf
     1.0.0.0/32 is subnetted, 1 subnets
O       1.1.1.1 [110/3] via 10.1.1.14, 00:14:27, GigabitEthernet2/0
                [110/3] via 10.1.1.10, 00:07:56, GigabitEthernet1/0
     3.0.0.0/32 is subnetted, 1 subnets
O       3.3.3.3 [110/2] via 10.1.1.14, 00:14:27, GigabitEthernet2/0
     4.0.0.0/32 is subnetted, 1 subnets
O       4.4.4.4 [110/2] via 10.1.1.10, 00:07:56, GigabitEthernet1/0
     10.0.0.0/30 is subnetted, 5 subnets
O       10.1.1.0 [110/2] via 10.1.1.14, 00:14:27, GigabitEthernet2/0
O       10.1.1.4 [110/2] via 10.1.1.10, 00:07:56, GigabitEthernet1/0
O       10.1.1.20 [110/2] via 10.1.1.14, 00:14:27, GigabitEthernet2/0
                  [110/2] via 10.1.1.10, 00:06:10, GigabitEthernet1/0
PE2#
```

# Configuration de MPLS
For that i used the following script:
```python
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
```

```c
show mpls ldp neighbor
show mpls forwarding-table
show mpls ip binding
```


## PE1
```c
PE1#show mpls ldp neighbor
    Peer LDP Ident: 3.3.3.3:0; Local LDP Ident 1.1.1.1:0
	TCP connection: 3.3.3.3.47551 - 1.1.1.1.646
	State: Oper; Msgs sent/rcvd: 18/16; Downstream
	Up time: 00:03:32
	LDP discovery sources:
	  GigabitEthernet1/0, Src IP addr: 10.1.1.2
        Addresses bound to peer LDP Ident:
          10.1.1.21       10.1.1.2        10.1.1.14       3.3.3.3         
PE1#show mpls forwarding-table
Local  Outgoing      Prefix            Bytes Label   Outgoing   Next Hop    
Label  Label or VC   or Tunnel Id      Switched      interface              
16     17            2.2.2.2/32        0             Gi1/0      10.1.1.2    
       No Label      2.2.2.2/32        0             Gi2/0      10.1.1.6    
17     Pop Label     3.3.3.3/32        0             Gi1/0      10.1.1.2    
18     No Label      4.4.4.4/32        0             Gi2/0      10.1.1.6    
19     No Label      10.1.1.8/30       0             Gi2/0      10.1.1.6    
20     Pop Label     10.1.1.12/30      0             Gi1/0      10.1.1.2    
21     Pop Label     10.1.1.20/30      0             Gi1/0      10.1.1.2    
       No Label      10.1.1.20/30      0             Gi2/0      10.1.1.6    
PE1#show mpls ip binding
  1.1.1.1/32 
	in label:     imp-null  
	out label:    16        lsr: 3.3.3.3:0       
  2.2.2.2/32 
	in label:     16        
	out label:    17        lsr: 3.3.3.3:0        inuse
  3.3.3.3/32 
	in label:     17        
	out label:    imp-null  lsr: 3.3.3.3:0        inuse
  4.4.4.4/32 
	in label:     18        
	out label:    18        lsr: 3.3.3.3:0       
  10.1.1.0/30 
	in label:     imp-null  
	out label:    imp-null  lsr: 3.3.3.3:0       
  10.1.1.4/30 
	in label:     imp-null  
	out label:    19        lsr: 3.3.3.3:0       
  10.1.1.8/30 
	in label:     19        
	out label:    20        lsr: 3.3.3.3:0       
  10.1.1.12/30 
	in label:     20        
        out label:    imp-null  lsr: 3.3.3.3:0        inuse
  10.1.1.20/30 
	in label:     21        
	out label:    imp-null  lsr: 3.3.3.3:0        inuse
  192.168.1.0/30 
	in label:     imp-null  
  192.168.1.4/30 
	in label:     imp-null  
PE1#

```

## PE2
```c
PE2#show mpls ldp neighbor
    Peer LDP Ident: 3.3.3.3:0; Local LDP Ident 2.2.2.2:0
	TCP connection: 3.3.3.3.54647 - 2.2.2.2.646
	State: Oper; Msgs sent/rcvd: 20/18; Downstream
	Up time: 00:05:44
	LDP discovery sources:
	  GigabitEthernet2/0, Src IP addr: 10.1.1.14
        Addresses bound to peer LDP Ident:
          10.1.1.21       10.1.1.2        10.1.1.14       3.3.3.3         
    Peer LDP Ident: 4.4.4.4:0; Local LDP Ident 2.2.2.2:0
	TCP connection: 4.4.4.4.34944 - 2.2.2.2.646
	State: Oper; Msgs sent/rcvd: 18/17; Downstream
	Up time: 00:04:36
	LDP discovery sources:
	  GigabitEthernet1/0, Src IP addr: 10.1.1.10
        Addresses bound to peer LDP Ident:
          10.1.1.22       10.1.1.10       10.1.1.6        4.4.4.4         
PE2#show mpls forwarding-table
Local  Outgoing      Prefix            Bytes Label   Outgoing   Next Hop    
Label  Label or VC   or Tunnel Id      Switched      interface              
16     16            1.1.1.1/32        0             Gi1/0      10.1.1.10   
       16            1.1.1.1/32        0             Gi2/0      10.1.1.14   
17     Pop Label     3.3.3.3/32        0             Gi2/0      10.1.1.14   
18     Pop Label     4.4.4.4/32        0             Gi1/0      10.1.1.10   
19     Pop Label     10.1.1.0/30       0             Gi2/0      10.1.1.14   
20     Pop Label     10.1.1.4/30       0             Gi1/0      10.1.1.10   
21     Pop Label     10.1.1.20/30      0             Gi1/0      10.1.1.10   
       Pop Label     10.1.1.20/30      0             Gi2/0      10.1.1.14   
PE2#show mpls ip binding 
  1.1.1.1/32 
	in label:     16        
	out label:    16        lsr: 3.3.3.3:0        inuse
	out label:    16        lsr: 4.4.4.4:0        inuse
  2.2.2.2/32 
	in label:     imp-null  
	out label:    17        lsr: 3.3.3.3:0       
	out label:    17        lsr: 4.4.4.4:0       
  3.3.3.3/32 
	in label:     17        
	out label:    imp-null  lsr: 3.3.3.3:0        inuse
	out label:    18        lsr: 4.4.4.4:0       
  4.4.4.4/32 
	in label:     18        
	out label:    18        lsr: 3.3.3.3:0       
	out label:    imp-null  lsr: 4.4.4.4:0        inuse
  10.1.1.0/30 
	in label:     19        
	out label:    imp-null  lsr: 3.3.3.3:0        inuse
	out label:    19        lsr: 4.4.4.4:0       
  10.1.1.4/30 
	in label:     20        
	out label:    19        lsr: 3.3.3.3:0       
        out label:    imp-null  lsr: 4.4.4.4:0        inuse
  10.1.1.8/30 
	in label:     imp-null  
	out label:    20        lsr: 3.3.3.3:0       
	out label:    imp-null  lsr: 4.4.4.4:0       
  10.1.1.12/30 
	in label:     imp-null  
	out label:    imp-null  lsr: 3.3.3.3:0       
	out label:    20        lsr: 4.4.4.4:0       
  10.1.1.20/30 
	in label:     21        
	out label:    imp-null  lsr: 3.3.3.3:0        inuse
	out label:    imp-null  lsr: 4.4.4.4:0        inuse
  192.168.1.8/30 
	in label:     imp-null  
  192.168.1.12/30 
	in label:     imp-null  
PE2#

```

## P1
```c
P1#show mpls ldp neighbor   
    Peer LDP Ident: 1.1.1.1:0; Local LDP Ident 3.3.3.3:0
	TCP connection: 1.1.1.1.646 - 3.3.3.3.47551
	State: Oper; Msgs sent/rcvd: 17/20; Downstream
	Up time: 00:05:19
	LDP discovery sources:
	  GigabitEthernet2/0, Src IP addr: 10.1.1.1
        Addresses bound to peer LDP Ident:
          10.1.1.1        10.1.1.5        192.168.1.1     192.168.1.5     
          1.1.1.1         
    Peer LDP Ident: 2.2.2.2:0; Local LDP Ident 3.3.3.3:0
	TCP connection: 2.2.2.2.646 - 3.3.3.3.54647
	State: Oper; Msgs sent/rcvd: 17/19; Downstream
	Up time: 00:05:01
	LDP discovery sources:
	  GigabitEthernet3/0, Src IP addr: 10.1.1.13
        Addresses bound to peer LDP Ident:
          10.1.1.9        10.1.1.13       192.168.1.9     192.168.1.13    
          2.2.2.2         
    Peer LDP Ident: 4.4.4.4:0; Local LDP Ident 3.3.3.3:0
	TCP connection: 4.4.4.4.47529 - 3.3.3.3.646
	State: Oper; Msgs sent/rcvd: 16/16; Downstream
	Up time: 00:04:00
	LDP discovery sources:
          GigabitEthernet1/0, Src IP addr: 10.1.1.22
        Addresses bound to peer LDP Ident:
          10.1.1.22       10.1.1.10       10.1.1.6        4.4.4.4         
P1#show mpls forwarding-table
Local  Outgoing      Prefix            Bytes Label   Outgoing   Next Hop    
Label  Label or VC   or Tunnel Id      Switched      interface              
16     Pop Label     1.1.1.1/32        0             Gi2/0      10.1.1.1    
17     Pop Label     2.2.2.2/32        0             Gi3/0      10.1.1.13   
18     Pop Label     4.4.4.4/32        0             Gi1/0      10.1.1.22   
19     Pop Label     10.1.1.4/30       0             Gi2/0      10.1.1.1    
       Pop Label     10.1.1.4/30       0             Gi1/0      10.1.1.22   
20     Pop Label     10.1.1.8/30       0             Gi3/0      10.1.1.13   
       Pop Label     10.1.1.8/30       0             Gi1/0      10.1.1.22   
P1#show mpls ip binding      
  1.1.1.1/32 
	in label:     16        
	out label:    imp-null  lsr: 1.1.1.1:0        inuse
	out label:    16        lsr: 2.2.2.2:0       
	out label:    16        lsr: 4.4.4.4:0       
  2.2.2.2/32 
	in label:     17        
	out label:    16        lsr: 1.1.1.1:0       
	out label:    imp-null  lsr: 2.2.2.2:0        inuse
	out label:    17        lsr: 4.4.4.4:0       
  3.3.3.3/32 
	in label:     imp-null  
	out label:    17        lsr: 1.1.1.1:0       
	out label:    17        lsr: 2.2.2.2:0       
	out label:    18        lsr: 4.4.4.4:0       
  4.4.4.4/32 
	in label:     18        
	out label:    18        lsr: 1.1.1.1:0       
	out label:    18        lsr: 2.2.2.2:0       
	out label:    imp-null  lsr: 4.4.4.4:0        inuse
  10.1.1.0/30 
	in label:     imp-null  
	out label:    imp-null  lsr: 1.1.1.1:0       
        out label:    19        lsr: 2.2.2.2:0       
	out label:    19        lsr: 4.4.4.4:0       
  10.1.1.4/30 
	in label:     19        
	out label:    imp-null  lsr: 1.1.1.1:0        inuse
	out label:    20        lsr: 2.2.2.2:0       
	out label:    imp-null  lsr: 4.4.4.4:0        inuse
  10.1.1.8/30 
	in label:     20        
	out label:    19        lsr: 1.1.1.1:0       
	out label:    imp-null  lsr: 2.2.2.2:0        inuse
	out label:    imp-null  lsr: 4.4.4.4:0        inuse
  10.1.1.12/30 
	in label:     imp-null  
	out label:    20        lsr: 1.1.1.1:0       
	out label:    imp-null  lsr: 2.2.2.2:0       
	out label:    20        lsr: 4.4.4.4:0       
  10.1.1.20/30 
	in label:     imp-null  
	out label:    21        lsr: 1.1.1.1:0       
	out label:    21        lsr: 2.2.2.2:0       
	out label:    imp-null  lsr: 4.4.4.4:0       
  192.168.1.0/30 
        out label:    imp-null  lsr: 1.1.1.1:0       
  192.168.1.4/30 
	out label:    imp-null  lsr: 1.1.1.1:0       
  192.168.1.8/30 
	out label:    imp-null  lsr: 2.2.2.2:0       
  192.168.1.12/30 
	out label:    imp-null  lsr: 2.2.2.2:0       
P1#

```

## P2
```c
P2#show mpls ldp neighbor
    Peer LDP Ident: 3.3.3.3:0; Local LDP Ident 4.4.4.4:0
	TCP connection: 3.3.3.3.646 - 4.4.4.4.47529
	State: Oper; Msgs sent/rcvd: 17/17; Downstream
	Up time: 00:05:07
	LDP discovery sources:
	  GigabitEthernet1/0, Src IP addr: 10.1.1.21
        Addresses bound to peer LDP Ident:
          10.1.1.21       10.1.1.2        10.1.1.14       3.3.3.3         
    Peer LDP Ident: 2.2.2.2:0; Local LDP Ident 4.4.4.4:0
	TCP connection: 2.2.2.2.646 - 4.4.4.4.34944
	State: Oper; Msgs sent/rcvd: 17/19; Downstream
	Up time: 00:05:00
	LDP discovery sources:
	  GigabitEthernet2/0, Src IP addr: 10.1.1.9
        Addresses bound to peer LDP Ident:
          10.1.1.9        10.1.1.13       192.168.1.9     192.168.1.13    
          2.2.2.2         
P2#show mpls forwarding-table
Local  Outgoing      Prefix            Bytes Label   Outgoing   Next Hop    
Label  Label or VC   or Tunnel Id      Switched      interface              
16     No Label      1.1.1.1/32        0             Gi3/0      10.1.1.5    
17     Pop Label     2.2.2.2/32        0             Gi2/0      10.1.1.9    
18     Pop Label     3.3.3.3/32        0             Gi1/0      10.1.1.21   
19     Pop Label     10.1.1.0/30       0             Gi1/0      10.1.1.21   
       No Label      10.1.1.0/30       0             Gi3/0      10.1.1.5    
20     Pop Label     10.1.1.12/30      0             Gi2/0      10.1.1.9    
       Pop Label     10.1.1.12/30      0             Gi1/0      10.1.1.21   
P2#show mpls ip binding 
  1.1.1.1/32 
	in label:     16        
	out label:    16        lsr: 3.3.3.3:0       
	out label:    16        lsr: 2.2.2.2:0       
  2.2.2.2/32 
	in label:     17        
	out label:    17        lsr: 3.3.3.3:0       
	out label:    imp-null  lsr: 2.2.2.2:0        inuse
  3.3.3.3/32 
	in label:     18        
	out label:    imp-null  lsr: 3.3.3.3:0        inuse
	out label:    17        lsr: 2.2.2.2:0       
  4.4.4.4/32 
	in label:     imp-null  
	out label:    18        lsr: 3.3.3.3:0       
	out label:    18        lsr: 2.2.2.2:0       
  10.1.1.0/30 
	in label:     19        
	out label:    imp-null  lsr: 3.3.3.3:0        inuse
	out label:    19        lsr: 2.2.2.2:0       
  10.1.1.4/30 
	in label:     imp-null  
	out label:    19        lsr: 3.3.3.3:0       
        out label:    20        lsr: 2.2.2.2:0       
  10.1.1.8/30 
	in label:     imp-null  
	out label:    20        lsr: 3.3.3.3:0       
	out label:    imp-null  lsr: 2.2.2.2:0       
  10.1.1.12/30 
	in label:     20        
	out label:    imp-null  lsr: 3.3.3.3:0        inuse
	out label:    imp-null  lsr: 2.2.2.2:0        inuse
  10.1.1.20/30 
	in label:     imp-null  
	out label:    imp-null  lsr: 3.3.3.3:0       
	out label:    21        lsr: 2.2.2.2:0       
  192.168.1.8/30 
	out label:    imp-null  lsr: 2.2.2.2:0       
  192.168.1.12/30 
	out label:    imp-null  lsr: 2.2.2.2:0       
P2#
```

# Configuration de VRF
For that we used the following script:
```python
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
```

## PE1

### Part 1:
```c
ip vrf VPN_Customer1
rd 100 :1
route-target both 100:1
ip vrf VPN_Customer2
rd 100 :2
route-target both 100:2
```
### Part 2 (Activation)
```c
interface g3/0
ip vrf forwarding VPN_Customer1
ip address 192.168.1.1 255.255.255.252
no shutdown

interface g4/0
ip vrf forwarding VPN_Customer2
ip address 192.168.1.5 255.255.255.252
no shutdown
```

## PE2

### Part 1:
```c
ip vrf VPN_Customer1
rd 100 :1
route-target both 100:1
ip vrf VPN_Customer2
rd 100 :2
route-target both 100:2
```
### Part 2 (Activation)
```c
interface g3/0
ip vrf forwarding VPN_Customer1
ip address 192.168.1.9 255.255.255.252
no shutdown

interface g4/0
ip vrf forwarding VPN_Customer2
ip address 192.168.1.13 255.255.255.252
no shutdown
```

# Configuration les interfaces et OSPF au niveau CE
## Interface Configration
Please note that interface configuration for all routers made by the first step of this walkthrough.
##  CE11
```c
CE11#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                unassigned      YES unset  administratively down down    
GigabitEthernet0/0         unassigned      YES unset  administratively down down    
GigabitEthernet1/0         192.168.1.2     YES manual up                    up      
GigabitEthernet2/0         unassigned      YES unset  administratively down down    
SSLVPN-VIF0                unassigned      NO  unset  up                    up      
Loopback0                  172.16.11.11    YES manual up                    up      
CE11#
```
## CE12
```c
CE12#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                unassigned      YES unset  administratively down down    
GigabitEthernet0/0         unassigned      YES unset  administratively down down    
GigabitEthernet1/0         192.168.1.10    YES manual up                    up      
GigabitEthernet2/0         unassigned      YES unset  administratively down down    
SSLVPN-VIF0                unassigned      NO  unset  up                    up      
Loopback0                  172.16.12.12    YES manual up                    up      
CE12#

```
## CE21
```c
CE21#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                unassigned      YES unset  administratively down down    
GigabitEthernet0/0         unassigned      YES unset  administratively down down    
GigabitEthernet1/0         192.168.1.6     YES manual up                    up      
GigabitEthernet2/0         unassigned      YES unset  administratively down down    
SSLVPN-VIF0                unassigned      NO  unset  up                    up      
Loopback0                  172.16.21.21    YES manual up                    up      
CE21#
```

## CE22
```c
CE22#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                unassigned      YES unset  administratively down down    
GigabitEthernet0/0         unassigned      YES unset  administratively down down    
GigabitEthernet1/0         192.168.1.14    YES manual up                    up      
GigabitEthernet2/0         unassigned      YES unset  administratively down down    
SSLVPN-VIF0                unassigned      NO  unset  up                    up      
Loopback0                  172.16.22.22    YES manual up                    up      
CE22#
```
## OSPF
For that we used the following script:
```python
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
```

# Configuration de MP_BGP
The following script has been used to configure both routers:
```python
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

```
Useful Commands:
```c
1- Show ip bgp vpnv4 vrf VPN_Customer1: Affichage Instance BGP
2- Show ip bgp vpnv4 vrf VPN_Customer2: Affichage Instance BGP
3- Show ip route vrf VPN_Customer1: Affichage la table de routage de
VRF de VPN_Customer1
4- Show ip route vrf VPN_Customer2: Affichage la table de routage de
VRF de VPN_Customer2
```

## Mentioned configuration on the script:
### PE1
```c
conf t
router bgp 100
no bgp default ipv4-unicast
neighbor 2.2.2.2 remote-as 100
neighbor 2.2.2.2 update-source loopback 0
address-family vpnv4 unicast
neighbor 2.2.2.2 activate
neighbor 2.2.2.2 send-community both
address-family ipv4 vrf VPN_Customer1
redistribute ospf 100 vrf VPN_Customer1
address-family ipv4 vrf VPN_Customer2
redistribute ospf 200 vrf VPN_Customer2
exit
exit
router ospf 100 vrf VPN_Customer1
redistribute bgp 100 subnets
network 192.168.1.0 0.0.0.3 area 12
router ospf 200 vrf VPN_Customer2
redistribute bgp 100 subnets
network 192.168.1.4 0.0.0.3 area 22
```

### PE2
```c
conf t
router bgp 100
no bgp default ipv4-unicast
neighbor 1.1.1.1 remote-as 100
neighbor 1.1.1.1 update-source loopback 0
address-family vpnv4 unicast
neighbor 1.1.1.1 activate
neighbor 1.1.1.1 send-community both
address-family ipv4 vrf VPN_Customer1
redistribute ospf 100 vrf VPN_Customer1
address-family ipv4 vrf VPN_Customer2
redistribute ospf 200 vrf VPN_Customer2
exit
exit
router ospf 100 vrf VPN_Customer1
redistribute bgp 100 subnets
network 192.168.1.8 0.0.0.3 area 12
router ospf 200 vrf VPN_Customer2
redistribute bgp 100 subnets
network 192.168.1.12 0.0.0.3 area 22
```

## Result
### PE1
```c
PE1#show ip bgp vpnv4 vrf VPN_Customer1
BGP table version is 17, local router ID is 1.1.1.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
Route Distinguisher: 100:1 (default for vrf VPN_Customer1)
*> 172.16.11.11/32  192.168.1.2              2         32768 ?
*>i172.16.12.12/32  2.2.2.2                  2    100      0 ?
*> 192.168.1.0/30   0.0.0.0                  0         32768 ?
*>i192.168.1.8/30   2.2.2.2                  0    100      0 ?
PE1#show ip bgp vpnv4 vrf VPN_Customer2
BGP table version is 17, local router ID is 1.1.1.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
Route Distinguisher: 100:2 (default for vrf VPN_Customer2)
*> 172.16.21.21/32  192.168.1.6              2         32768 ?
*>i172.16.22.22/32  2.2.2.2                  2    100      0 ?
*> 192.168.1.4/30   0.0.0.0                  0         32768 ?
*>i192.168.1.12/30  2.2.2.2                  0    100      0 ?
PE1#show ip route vrf VPN_Customer1

Routing Table: VPN_Customer1
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route

Gateway of last resort is not set

     172.16.0.0/32 is subnetted, 2 subnets
B       172.16.12.12 [200/2] via 2.2.2.2, 00:03:13
O       172.16.11.11 [110/2] via 192.168.1.2, 00:07:21, GigabitEthernet3/0
     192.168.1.0/30 is subnetted, 2 subnets
B       192.168.1.8 [200/0] via 2.2.2.2, 00:03:28
C       192.168.1.0 is directly connected, GigabitEthernet3/0
PE1#show ip route vrf VPN_Customer2

Routing Table: VPN_Customer2
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route

Gateway of last resort is not set

     172.16.0.0/32 is subnetted, 2 subnets
B       172.16.22.22 [200/2] via 2.2.2.2, 00:03:00
O       172.16.21.21 [110/2] via 192.168.1.6, 00:07:06, GigabitEthernet4/0
     192.168.1.0/30 is subnetted, 2 subnets
B       192.168.1.12 [200/0] via 2.2.2.2, 00:03:15
C       192.168.1.4 is directly connected, GigabitEthernet4/0
PE1#
```

### PE2
```c
PE2#show ip bgp vpnv4 vrf VPN_Customer1
BGP table version is 17, local router ID is 2.2.2.2
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
Route Distinguisher: 100:1 (default for vrf VPN_Customer1)
*>i172.16.11.11/32  1.1.1.1                  2    100      0 ?
*> 172.16.12.12/32  192.168.1.10             2         32768 ?
*>i192.168.1.0/30   1.1.1.1                  0    100      0 ?
*> 192.168.1.8/30   0.0.0.0                  0         32768 ?
PE2#show ip bgp vpnv4 vrf VPN_Customer2
BGP table version is 17, local router ID is 2.2.2.2
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
Route Distinguisher: 100:2 (default for vrf VPN_Customer2)
*>i172.16.21.21/32  1.1.1.1                  2    100      0 ?
*> 172.16.22.22/32  192.168.1.14             2         32768 ?
*>i192.168.1.4/30   1.1.1.1                  0    100      0 ?
*> 192.168.1.12/30  0.0.0.0                  0         32768 ?
PE2#show ip route vrf VPN_Customer1

Routing Table: VPN_Customer1
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route

Gateway of last resort is not set

     172.16.0.0/32 is subnetted, 2 subnets
O       172.16.12.12 [110/2] via 192.168.1.10, 00:03:43, GigabitEthernet3/0
B       172.16.11.11 [200/2] via 1.1.1.1, 00:04:46
     192.168.1.0/30 is subnetted, 2 subnets
C       192.168.1.8 is directly connected, GigabitEthernet3/0
B       192.168.1.0 [200/0] via 1.1.1.1, 00:04:46
PE2#show ip route vrf VPN_Customer2

Routing Table: VPN_Customer2
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route

Gateway of last resort is not set

     172.16.0.0/32 is subnetted, 2 subnets
O       172.16.22.22 [110/2] via 192.168.1.14, 00:03:28, GigabitEthernet4/0
B       172.16.21.21 [200/2] via 1.1.1.1, 00:04:46
     192.168.1.0/30 is subnetted, 2 subnets
C       192.168.1.12 is directly connected, GigabitEthernet4/0
B       192.168.1.4 [200/0] via 1.1.1.1, 00:04:46
PE2#
```

## Final Network Check:
### PE1
```c
PE1#Show ip route
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route

Gateway of last resort is not set

     1.0.0.0/32 is subnetted, 1 subnets
C       1.1.1.1 is directly connected, Loopback0
     2.0.0.0/32 is subnetted, 1 subnets
O       2.2.2.2 [110/3] via 10.1.1.6, 01:40:47, GigabitEthernet2/0
                [110/3] via 10.1.1.2, 01:40:37, GigabitEthernet1/0
     3.0.0.0/32 is subnetted, 1 subnets
O       3.3.3.3 [110/2] via 10.1.1.2, 01:40:37, GigabitEthernet1/0
     4.0.0.0/32 is subnetted, 1 subnets
O       4.4.4.4 [110/2] via 10.1.1.6, 01:40:47, GigabitEthernet2/0
     10.0.0.0/30 is subnetted, 5 subnets
O       10.1.1.8 [110/2] via 10.1.1.6, 01:40:47, GigabitEthernet2/0
O       10.1.1.12 [110/2] via 10.1.1.2, 01:40:37, GigabitEthernet1/0
C       10.1.1.0 is directly connected, GigabitEthernet1/0
C       10.1.1.4 is directly connected, GigabitEthernet2/0
O       10.1.1.20 [110/2] via 10.1.1.6, 01:40:49, GigabitEthernet2/0
                  [110/2] via 10.1.1.2, 01:40:39, GigabitEthernet1/0
PE1#
```

### PE2
```c
PE2#sh ip route
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route

Gateway of last resort is not set

     1.0.0.0/32 is subnetted, 1 subnets
O       1.1.1.1 [110/3] via 10.1.1.14, 01:41:31, GigabitEthernet2/0
                [110/3] via 10.1.1.10, 01:41:31, GigabitEthernet1/0
     2.0.0.0/32 is subnetted, 1 subnets
C       2.2.2.2 is directly connected, Loopback0
     3.0.0.0/32 is subnetted, 1 subnets
O       3.3.3.3 [110/2] via 10.1.1.14, 01:41:31, GigabitEthernet2/0
     4.0.0.0/32 is subnetted, 1 subnets
O       4.4.4.4 [110/2] via 10.1.1.10, 01:41:41, GigabitEthernet1/0
     10.0.0.0/30 is subnetted, 5 subnets
C       10.1.1.8 is directly connected, GigabitEthernet1/0
C       10.1.1.12 is directly connected, GigabitEthernet2/0
O       10.1.1.0 [110/2] via 10.1.1.14, 01:41:31, GigabitEthernet2/0
O       10.1.1.4 [110/2] via 10.1.1.10, 01:41:42, GigabitEthernet1/0
O       10.1.1.20 [110/2] via 10.1.1.14, 01:41:32, GigabitEthernet2/0
                  [110/2] via 10.1.1.10, 01:41:42, GigabitEthernet1/0
PE2#
```

## PIG TEST
```c
CE11#ping 172.16.12.12

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 172.16.12.12, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 44/52/72 ms
CE11#
```
