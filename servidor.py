import socket
import threading

ServerIP = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    username = "servidor"
    client.connect((ServerIP,PORT))
    print(f'Connected Successfully to {ServerIP}:{PORT}')
except:
    print(f'ERROR: Please review your input: {ServerIP}:{PORT}')
def toArray (pacote):
   array = pacote.split('#')
   return array
def receiveMessage():
    while True:
        try:
            message = client.recv(2048).decode('ascii')
            if message=='getUser':
                client.send(username.encode('ascii'))
            else:
                print("Mensagem recebida e armazenada: "+ message)
                msg = toArray(message)
                if(msg[0] == "0"):
                  arquivos.append(msg[1])
                  dono.append(msg[2])
                  mensg = 'Arquivo "'+ msg[1] +'" armazenado com sucesso'
                  client.send(mensg.encode('ascii'))
                  #print(message)
                elif (msg[0] == "1"):
                   if msg[1] in arquivos:
                      mensg = 'Arquivo "'+ arquivos[arquivos.index(msg[1])] +'" recuperado com sucesso' 
                      client.send(mensg.encode('ascii'))
                   if msg[1] not in arquivos: 
                      client.send('Arquivo não encontrado'.encode('ascii'))
                      #print(message)
                      
                
        except:
            print('ERROR: Check your connection or server might be offline')

arquivos = []
dono = []
thread1 = threading.Thread(target=receiveMessage,args=()) 

thread1.start()
