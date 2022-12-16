import socket
import threading
import os

ServerIP = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    side = "client"
    client.connect((ServerIP,PORT))
    print(f'Connected Successfully to {ServerIP}:{PORT}')
except:
    print(f'ERROR: Please review your input: {ServerIP}:{PORT}')

def receiveMessage():
    while True:
        try:
            message = client.recv(2048).decode('ascii')
            if message=='getUser':
                client.send(side.encode('ascii'))
            else:
                print(message)
        except:
            print('ERROR: Check your connection or server might be offline')

def sendMessage0(operacao,arquivo,donoDoDeposito,nivel):
   pacote = operacao+"#"+arquivo+"#"+str(donoDoDeposito)+"#"+str(nivel)
   client.send(pacote.encode('ascii'))
def sendMessage1(operacao,arquivo,donoDoDeposito):
   pacote = operacao+"#"+arquivo+"#"+str(donoDoDeposito)
   client.send(pacote.encode('ascii'))

menu=True

while(menu == True):
   print(f'########################################################')
   print(f'############### Sistema de armazenamento ###############')
   print(f'###    0 - Depósito do arquivo')
   print(f'###    1 - Recuperação do arquivo')
   print(f'###    2 - Encerrar')
   entrada = int(input())
   match entrada:
      case 0:
         print(f'###    Digite o nome do arquivo')
         arquivo = input()
         print(f'###    Digite o nível de tolerância a falhas')
         nivel = int(input())
         donoDoDeposito = os.getpid()
         thread1 = threading.Thread(target=receiveMessage,args=()) 
         thread2 = threading.Thread(target=sendMessage0,args=("0",arquivo,donoDoDeposito,nivel))
         thread1.start()
         thread2.start()
      case 1:
         print(f'###    Digite o nome do arquivo')
         arquivo = input()
         donoDoDeposito = os.getpid()
         thread1 = threading.Thread(target=receiveMessage,args=()) 
         thread2 = threading.Thread(target=sendMessage1,args=("1",arquivo,donoDoDeposito))
         thread1.start()
         thread2.start()
      case 2:
         print(f'Encerrando...')
         menu = False
      case _:
         print(f'Tente novamente')