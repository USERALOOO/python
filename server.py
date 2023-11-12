from socket import *
import sys 
import threading



serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', 9900))


activeConnections = {'connections': 0}


def handle_client(connectionSocket, addr):
   
    
    try:
        message = connectionSocket.recv(1024).decode()
       
        #print(message.split())
        #print('')
        #print('')
        if len(message.split()):
            filename = message.split()[1]
            if filename == '/HelloWorld.html':
                 activeConnections['connections']+=1
                 print(f"[Active Connections] {activeConnections}")
            
            f = open(filename[1: ])
            outputdata = f.read().split()

            connectionSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n','UTF-8'))

            #Send one HTTP header line into socket
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

            print('success')
        
            connectionSocket.close()

    except IOError:
        connectionSocket.send(bytes('HTTP/1.1 404 Not Found\r\n\r\n','UTF-8'))
        connectionSocket.send('<body bgcolor="white"><h1>404 Not Found</h1></body>'.encode())
        connectionSocket.close()




def start():
    
    serverSocket.listen()
    
    while True:
       
        print('Ready To serve..')
        connectionSocket, addr = serverSocket.accept()
        thread = threading.Thread(target=handle_client, args=[connectionSocket, addr])
        thread.start()

        



    
    
       
        

start()
serverSocket.close()

sys.exit()#Terminate the program after sending the corresponding data

