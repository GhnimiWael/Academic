#!/usr/bin/env python2
import subprocess
from time import *

print("""

____________  ___  _________ _      _____ 
| ___ \\ ___ \\ |  \\/  || ___ \\ |    /  ___|
| |_/ / |_/ / | .  . || |_/ / |    \\ `--. 
| ___ \\ ___ \\ | |\\/| ||  __/| |     `--. \\
| |_/ / |_/ / | |  | || |   | |____/\\__/ /
\\____/\\____/  \\_|  |_/\\_|   \\_____/\\____/ 
                                          
      Welcom To BB MPLS Automated by W43L <3                                     
""")

print("[*] Running base routers configuration (ADDRESSING) ... ")
subprocess.call(["python2", "base_config.py"])
print("[+] Base configurations completed successfuly!")
print("================[*] LOADING NEXT [*] ============================\n")
sleep(2)

print("[*] Running OSPF BackBone configurations ... ")
subprocess.call(["python2", "ospf_config.py"])
print("[+] OSPF BackBone configurations completed successfuly!")
print("================[*] LOADING NEXT [*] ============================\n")
sleep(2)

print("[*] Running MPLS configurations ... ")
subprocess.call(["python2", "mpls_config.py"])
print("[+] Base configurations completed successfuly!")
print("================[*] LOADING NEXT [*] ============================\n")
sleep(2)

print("[*] Running VRF configurations ... ")
subprocess.call(["python2", "VRF_config.py"])
print("[+] VRF configurations completed successfuly!")
print("================[*] LOADING NEXT [*] ============================\n")
sleep(2)

print("[*] Running OSPF configurations for CEij Routers ... ")
subprocess.call(["python2", "ospf_CEij_config_v2.py"])
print("[+] OSPF configurations for CEij Routers completed successfuly!\n")
print("================[*] LOADING NEXT [*] ============================\n")
sleep(2)

print("[*] Running MP_BGP configurations ... ")
subprocess.call(["python2", "MP_BGP_PE1.py"])
print("[+] MP_BGP configurations completed successfuly!\n\n")

print("====================================================================")
print("[+] PROCESS COMPLETED SUCCESSFULY ! - THANK'S FOR YOUR TIME <3 [+]")
print("====================================================================")

"""
telnet 127.0.0.1 5000
telnet 127.0.0.1 5001
telnet 127.0.0.1 5002
telnet 127.0.0.1 5003
telnet 127.0.0.1 5004
telnet 127.0.0.1 5005
telnet 127.0.0.1 5006
telnet 127.0.0.1 5007
p1 -> 10.1.1.13 -> PE2
"""