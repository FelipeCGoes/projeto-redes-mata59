import socket
import threading

HOST = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
print(f'Server is Up and Listening on {HOST}:{PORT}')

clients = []
usernames = []

servers = []
serversNames = []

def globalMessage(message):
   
   txt = servers[0]
   txt.send(message)
   
def globalM(message):
   txt = clients[0]
   txt.send(message)

def handleMessages(client,username):
    while True:
        try:
           
            if username == "client":
               receiveMessageFromClient = client.recv(2048).decode('ascii')
               globalMessage(f'{receiveMessageFromClient}'.encode('ascii'))
            elif username == "servidor":
               receiveMessageFromClient = client.recv(2048).decode('ascii')
               globalM(f'{receiveMessageFromClient}'.encode('ascii'))
        except:
            client.close()


def initialConnection():
    while True:
        try:
            client, address = server.accept()
            print(f"New Connetion: {str(address)}")
            
            client.send('getUser'.encode('ascii'))
            username = client.recv(2048).decode('ascii')
            
            if username == "client":
               clients.append(client)
               usernames.append(username)
               user_thread = threading.Thread(target=handleMessages,args=(client,username,))
               user_thread.start()
            else:
               servers.append(client)
               serversNames.append(username)
               user_thread = threading.Thread(target=handleMessages,args=(client,username,))
               user_thread.start()
        except:
            pass

initialConnection()