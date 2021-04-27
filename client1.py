import cherrypy
import socket
import json
import sys

FORMAT = 'utf-8'
HEADER = 4096
ADDR = ("127.0.0.1", 3001)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send ():
    """
    Opening the json : matricules.json and sending it 
    to the server
    """
    with open("matricules.json") as file:
        msg = json.loads(file.read())
    
    msg.update(port = port) #change the port when launching the file
    msg = json.dumps(msg)       #transforing the dict into a string
    message = msg.encode(FORMAT)    #encoding in utf8
    msg_length = len(message)   
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(message)    #sending

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

class Server:
    def subscribe(self):
        pass

    def ping(self):
        send()
        return "pong"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8080
    site = f"http://localhost:{port}/ping"
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': port})
    cherrypy.quickstart(Server())