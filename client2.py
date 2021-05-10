import socket
from jsonNetwork import Timeout, sendJSON, receiveJSON, NotAJSONObject, fetch
from threading import Thread 
import sys
import json
import time
from collections import defaultdict
import random
import negamax

class game:
    def __init__(self,portClient,name='toto',portServer=3000):
        self.__name = name
        self.__port_client = int(portClient)
        self.__port_server = portServer
        self.__host = "127.0.0.1"
        self.__live = 0
    
    def subscribe(self):
        server_socket = socket.socket()                           # instantiate
        server_socket.connect((self.__host, self.__port_server))  # connect to the server
        sendJSON(server_socket,{"request":"subscribe","port":self.__port_client,"name":self.__name,"matricules":"20521"})
        subscription=True
        while subscription:
            data = receiveJSON(server_socket)
            print(data)
            if (data['response']=="ok"):
                subscription=False  
                return True
        return False
    
    def app(self):
        self.subscribe()
        ping=True
        client_socket = socket.socket()                              # Create a socket object
        client_socket.bind((self.__host, self.__port_client))        # Bind to the port
        client_socket.listen(5)
        while ping:
            #print("try")
            c,addr = client_socket.accept()
            #print('Got connection from', addr)    
            data=receiveJSON(c)
            if (data['request']=='ping'):
                sendJSON(c,{'response':'pong'})
            elif (data['request']=='play'):
                #print(data)
                nextMove=self.play(data)
                #print(nextMove)
                sendJSON(c,nextMove)
        c.close()

    def move(self,state):
        result=negamax.think(state)
        #nextMove=negamax.negamaxWithPruningIterativeDeepening(state,state['current'])
        #result={"response": "move",
	    #        "move": {'marbles':nextMove[1][0],'direction':nextMove[1][1]},
	    #        "message": "pass"}
        return result
    def play(self,data):
        if data['lives']>=1:
            nextMove=self.move(data['state'])
        return nextMove
    
    
        

def main(argv):
    #player=game(argv[1],argv[2])
    player=game(3002,"toto2")
    player.app()

if (__name__=="__main__"):
    main(sys.argv)