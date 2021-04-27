import socket
from jsonNetwork import Timeout, sendJSON, receiveJSON, NotAJSONObject, fetch
from threading import Thread 
import sys
import json
import time

def main(argv):
    assert(type(argv)) is list,str(type(argv))+ "got, exoected <list>"
    port_client=int(argv[1])
    port_server = 3000  # socket server port number
    host = "127.0.0.1"
    server_socket = socket.socket()  # instantiate
    server_socket.connect((host, port_server))  # connect to the server
    sendJSON(server_socket,{"request":"subscribe","port":port_client,"name":"toto","matricules":"20521"})
    subscription=True
    while subscription:
        data = receiveJSON(server_socket)
        print(data)
        if (data['response']=="ok"):
            subscription=False
    ping=True
    client_socket = socket.socket()                # Create a socket object
    client_socket.bind((host, port_client))        # Bind to the port
    client_socket.listen(5)
    while ping:
        print("try")
        c,addr = client_socket.accept()
        print('Got connection from', addr)    
        data=receiveJSON(c)
        print(data)
        if (data['request']=='ping'):
            sendJSON(c,{'response':'pong'})
            c.close()
        c.close()

if (__name__=="__main__"):
    main(sys.argv)

