import socket
from jsonNetwork import Timeout, sendJSON, receiveJSON, NotAJSONObject, fetch
from threading import Thread 
import sys
import json
import time

def main(argv):
    assert(type(argv)) is list,str(type(argv))+ "got, exoected <list>"
    port=int(argv[1])
    host = socket.gethostname()  # as both code is running on same pc
    #port = 3000  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect(("127.0.0.1", port))  # connect to the server
    sendJSON(client_socket,{"request":"subscribe","port":port,"name":"toto","matricules":"20521"})
    subscription=False
    while subscription:
        data = receiveJSON(client_socket)
        if (data['response']=="ok"):
            subscription=True
        print("passe la")
    ping=True
    while ping:
        #client_socket.send(message.encode())  # send message
        #data = client_socket.recv(1024).decode()  # receive response
        #data = json.loads(data)
        print("another loop")
        try :
            data = receiveJSON(client_socket)
            print("try passed")
        except :
            pass
        if (subscription==True):
            print(subscription)
            if (data["request"]=="ping"):
                sendJSON(client_socket,{"response":'pong'})
                print("send a pong to ;", )
                data.clear()
                ping=False

    # server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # adress_server = ("127.0.0.1",port)
    # connect(server,adress_server)
    # sendJSON(server,{"request":"subscribe","port":port,"name":"toto","matricules":"20521"})
    # #askSubscribe(client,3000) 
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.bind(("0.0.0.0", 3001))
    # sock.listen()
    # print("try 1")
    # while True:
    #     # Wait for a connection
    #     connection, server_address = sock.accept()
    #     data = connection.recv(4096).decode('utf8')
    #     print(type(data),data)
    #     data = json.loads(data)
    #     print(type(data),data)
    #     if (data["request"]=="ping"):
    #         sendJSON(connection,{"response":'pong'})
    #         print("send a pong to ;", )
    #         data.clear()

# def processRequest(client, address):
#     '''
#     Route request to request handlers
#     '''
#     print('request from', address)
#     try:
#         request = receiveJSON(client)
#         print(request)
        
#     except Timeout:
#         sendJSON(client, {
#             'response': 'error',
#             'error': 'transmition take too long'
#         })

# def fetch(address, data, timeout=1):
#     '''
#         Request response from address. Data is included in the request
#     '''
#     client = socket.socket()
#     client.connect(address)
#     #sendJSON(client, data)
#     response = receiveJSON(client, timeout)
#     print(response)
#     return response

    
# def connect(s,address):
#     # connect to server
#     try:    
#         s.connect(address)
#     except :
#         print("connection failed")

# def askSubscribe(client,port):
#     # subscribe to server
#     msg = {"request":"subscribe","port":port,"name":"toto","matricules":"20521"}
#     msg = json.dumps(msg)
#     msg = msg.encode("utf8")
#     total = 0
#     try :
#         while total < len(msg):
#             sent = client.send(msg[total:])
#             total += sent
#     except :
#         print("subscribtion failed")


# def send(client,port,FORMAT):
#     """
#     Opening the json : matricules.json and sending it 
#     to the server
#     """
#     with open("matricules.json") as file:
#         msg = json.loads(file.read()) 
#     msg.update(port = port) #change the port when launching the file
#     msg = json.dumps(msg)       #transforing the dict into a string
#     message = msg.encode("utf8")    #encoding in utf8
#     try :
#         while total < len(msg):
#             sent = client.send(msg[total:])
#             total += sent
#     except :
#         print("send failed")    #sending

# def sendmove(address, timeout=1):
#     '''
#     Request response from address. Data is included in the request
#     '''
#     socket = s.socket()
#     socket.connect(address)
#     msg = {"marbles": [[1, 1], [2, 2]],"direction": "SE"}
#     msg = json.dumps(msg)
#     msg = msg.encode("utf8")
#     socket.send(msg)
#     response = receiveJSON(socket, timeout)
#     print(response)
#     return response

# def stopSubscriptions():
#     pass



# class NotAJSONObject(Exception):
#     pass

# class Timeout(Exception):
#     pass

# def sendJSON(socket, obj):
#     message = json.dumps(obj)
#     if message[0] != '{':
#         raise NotAJSONObject('sendJSON support only JSON Object Type')
#     print(message)
#     message = message.encode('utf8')   
#     total = 0
#     while total < len(message):
#         sent = socket.send(message[total:])
#         total += sent

# def receiveJSON(socket, timeout = 50):
#     finished = False
#     message = ''
#     data = ''
#     start = time.time()
#     while not finished:
#         message += socket.recv(4096).decode('utf8')
#         if len(message) > 0 and message[0] != '{':
#             raise NotAJSONObject('Received message is not a JSON Object')
#         try:
#             data = json.loads(message)
#             finished = True
#         except json.JSONDecodeError:
#             if time.time() - start > timeout:
#                 raise Timeout()
#     return data



if (__name__=="__main__"):
    main(sys.argv)

