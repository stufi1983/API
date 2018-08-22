#!/usr/bin/python2.7
import socket
import requests
import MySQLdb

#Play Audio
import audiotest
words=[]
words.append("/usr/share/sounds/alsa/Front_Left.wav")
words.append("/usr/share/sounds/alsa/Front_Right.wav")

for word in words:
  audiotest.play_music(word)

##########Database Connection###############
# Open database connection
db = MySQLdb.connect("localhost","root","winda1984","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()

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