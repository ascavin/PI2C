import pygame
import socket
import sys



def main(argv):
    assert(type(argv)) is list,str(type(argv))+ "got, exoected <list>"
    current_state=["INIT"]
    port=argv[0]
    s = socket.socket()
    connect(s,port)       #connect to server
    AskSubscribe(s,port)   #subscribe to server
    current_state=["WAIT"]
    pass

def connect(s,port):
    # connect to server
    try:    
        s.connect(('localhost',port))
    except :
        print("connection failed")   

def AskSubscribe(s,port):
    # subscribe to server
    msg = "{subscribe}".encode('utf8')
    try :
        s.sendto(msg, ('localhost',port))
    except :
        print("subscribtion failed")

if (__name__=="__main__"):
    if(len.sys.argv>1)
        main(sys.argv)
    else(main(sys.argv+["4000"]))
