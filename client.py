import pygame
import socket as s
from jsonNetwork import Timeout, sendJSON, receiveJSON, NotAJSONObject, fetch
import sys
import json

def main(argv):
    assert(type(argv)) is list,str(type(argv))+ "got, exoected <list>"
    port=argv[0]
    socket = s.socket()
    socket.connect((("127.0.0.1",3000)))
    msg = {"request":"subscribe","port":"3000","name":"toto","matricules":"20521"}
    msg = json.dumps(msg)
    msg = msg.encode("utf8")
    total = 0
    while total < len(msg):
        sent = socket.send(msg[total:])
        total += sent
    #sendJSON(socket,{'request':'subscribe','subscribe':'subscribe'})
    #connect(s,port)       #connect to server
    #askSubscribe(s,port)   #subscribe to server
    pass

def connect(s,port):
    # connect to server
    try:    
        s.connect(('localhost',port))
    except :
        print("connection failed")

def askSubscribe(client,port):
    # subscribe to server
    msg = "{subscribe}".encode('utf8')
    try :
        client.sendto(msg, ('localhost',port))
        sendJSON(client,{['suscribe']})
    except :
        print("subscribtion failed")

def stopSubscriptions():
    pass
if (__name__=="__main__"):
    main(sys.argv)

