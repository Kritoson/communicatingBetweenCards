import socket

UDP_IP = "CHANGE TO PI'S IP"

UDP_Port = 5005

MESSAGE = "Hello, World!"

print ("UDP target IP:", UDP_IP)

print ("UDP target port:", UDP_Port)

print ("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet

socket.SOCK_DGRAM) # UDP

sock.sendto(MESSAGE, (UDP_IP, UDP_Port))