import socket
import datetime

target= input("Enter target IP adress: ")

print(f"Scanning {target}")
print(f"Scan started at {datetime.datetime.now()}")

open_ports=[]


for port in range(1,1025):
    s = socket.socket()
    s.settimeout(0.1)
    if s.connect_ex((target,port))==0:
        print(f"Port {port} is open")
        open_ports.append(port)
    s.close()

print(f"Scan ended at : {datetime.datetime.now()}")

with open ("results.txt","w") as f:
    f.write(f"Scan results for {target}\n")
    for port in open_ports:
        f.write(f"Port {port} is open\n")

print("Results saved to results.txt")
