import socket
import datetime

target= input("Enter target IP adress: ")

print(f"Scanning {target}")


for port in range(1,1025):
    s = socket.socket()
    s.settimeout(0.1)
    if s.connect_ex((target,port))==0:
        print(f"Port {port} is open")
    s.close()

print(f"Scan started at : {datetime.datetime.now()}")
