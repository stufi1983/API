#!/usr/bin/python2.7
import socket
import requests

UDP_PORT = 50000
UDP_IP = ""

sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print (data)

    if data[0:1]==b'T':
        socksend = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        socksend.sendto(bytes(":Loket:", "utf-8"), (data[3:], 51000))

    try:
        r = requests.head("http://localhost/cgi-bin/test")
        # print(r.status_code)
        # prints the int of the status code. Find more at httpstatusrappers.com :)
    except requests.ConnectionError:
        print("failed to connect")
