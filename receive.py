import socket

UDP_IP = "CHANGE TO PI'S IP"

UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet

socket.SOCK_DGRAM) # UDP

sock.bind("Hi I am Mustafa", (UDP_IP, UDP_PORT))

while True:

    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

    print ("received message:",data)