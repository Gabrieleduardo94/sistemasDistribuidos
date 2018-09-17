#!/usr/bin/python3

###
#  Import socket module
#  
import socket 
  
def Main(): 
    ###
    # local host IP '127.0.0.1'
    #  
    host = input("\nDigite o IP de servidor: ")
  
    ###
    #  Define the port on which you want to connect
    #  
    port = 12345 
  
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  
        ###
        #  connect to server on local computer
        #  
        s.connect((host,port)) 
  
        ###
        #  message you send to server
        #  
        message = input("\nDigite aqui sua mensagem: ")
        while True: 
  
            ###
            #  message sent to server
            #  
            s.send(message.encode('ascii')) 
  
            ### 
            # messaga received from server
            #  
            data = s.recv(1024) 
  
            ###
            #  print the received message 
            #  here it would be a reverse of sent message
            #  
            print('Recebeu do servidor :',str(data.decode('ascii'))) 
  
            ###
            # ask the client whether he wants to continue
            #   
            ans = input('\nQuer mandar outra mensagem? (s/n) :') 
            if ans == 's': 
                continue
            else: 
                break
     
     
  
if __name__ == '__main__': 
    Main() 
