import pygame
import socket as s
from jsonNetwork import Timeout, sendJSON, receiveJSON, NotAJSONObject, fetch
import sys
import json

def main(argv):
    assert(type(argv)) is list,str(type(argv))+ "got, exoected <list>"
    port=int(argv[1])
    socket = s.socket()
    outComingAddress = ("127.0.0.1",port)
    inComingaddress = ("127.0.0.1",3000)
    connect(socket,outComingAddress)
    askSubscribe(socket,port)
    toPrint = ping(inComingaddress)

def connect(s,address):
    # connect to server
    try:    
        s.connect(address)
    except :
        print("connection failed")

def askSubscribe(client,port):
    # subscribe to server
    msg = {"request":"subscribe","port":port,"name":"toto","matricules":"20521"}
    msg = json.dumps(msg)
    msg = msg.encode("utf8")
    total = 0
    try :
        while total < len(msg):
            sent = client.send(msg[total:])
            total += sent
    except :
        print("subscribtion failed")

def ping(address, timeout=1):
    '''
    Request response from address. Data is included in the request
    '''
    socket = s.socket()
    socket.connect(address)
    msg = {"marbles": [[1, 1], [2, 2]],"direction": "SE"}
    msg = json.dumps(msg)
    msg = msg.encode("utf8")
    socket.send(msg)
    response = receiveJSON(socket, timeout)
    print(response)
    return response

def stopSubscriptions():
    pass

if (__name__=="__main__"):
    main(sys.argv)

