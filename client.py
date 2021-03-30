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

def incomingMessage():
    '''
		Route request to request handlers
	'''
	print('request from', address)
	try:
		request = receiveJSON(client)
		
		if request['request'] == 'subscribe':
			startSubscription(client, address, request)
		else:
			raise ValueError('Unknown request \'{}\''.format(request['request']))

	except Timeout:
		sendJSON(client, {
			'response': 'error',
			'error': 'transmition take too long'
		})
	except NotAJSONObject as e:
		sendJSON(client, {
			'response': 'error',
			'error': str(e)
		})
	except KeyError as e:
		sendJSON(client, {
			'response': 'error',
			'error': 'Missing key {}'.format(str(e))
		})
	except Exception as e:
		sendJSON(client, {
			'response': 'error',
			'error': str(e)
		})

def oucomingMessage():


if (__name__=="__main__"):
    if(len.sys.argv>1)
        main(sys.argv)
    else(main(sys.argv+["4000"]))
