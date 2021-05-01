import socket
from jsonNetwork import Timeout, sendJSON, receiveJSON, NotAJSONObject, fetch
from threading import Thread 
import sys
import json
import time
import movetest

class game:

    __current_state = "initialize"
    __name = "toto"
    __port_client = 3001
    __port_server = 3000
    __host = "127.0.0.1"

    def subscribe(self):

    def isMyTurn(self,data):
        if (data['players'][data["current"]]==self.__name):
            pass
        return False

    def checkLife(self,data):
        if (data['lives']>0):
            return True
        else : 
            return False



def main(argv):
    assert(type(argv)) is list,str(type(argv))+ "got, exoected <list>"
    port_client=int(argv[1])
    name=argv[2]
    port_server = 3000  # socket server port number
    host = "127.0.0.1"
    server_socket = socket.socket()  # instantiate
    server_socket.connect((host, port_server))  # connect to the server
    sendJSON(server_socket,{"request":"subscribe","port":port_client,"name":name,"matricules":"20521"})
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
        if (data['request']=='ping'):
            sendJSON(c,{'response':'pong'})
        elif (data['request']=='play'):
            print("data state :",data['state'])
            print("data['state']['current'] :",data['state']["current"])
            print("data['state']['players'][data['state']['current']] :",data['state']['players'][data['state']['current']])
            break
            # 
            # #isMyTurn(state)
            # readGridState()
            # computeMove(data['state'])
        c.close()



def readGridState():
    return False

def computeMove(grid):
    checkMove(grid)
    return False

def checkMove(grid):
    return False

def move(state):
    


if (__name__=="__main__"):
    main(sys.argv)

