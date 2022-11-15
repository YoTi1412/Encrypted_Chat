import scoket
import threading

import rsa


choice = input("Do you want to Host (1), or to connect (2): ")

if choice == '1':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.1.6", 4444))
    server.listen()
