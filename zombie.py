import socket
import threading
import os

bind_ip = "192.168.60.230"
bind_port = 8118
client=[]



server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print ("Le serveur attend une connexion")

def thread_recevoir_client(client_socket):
        while True:
            request = client_socket.recv(1024)
            print ("[*] Received: %s" %request )

def thread_connexion():
    while True:
        client2,addr=server.accept()
        client.append(client2)
        print ("[*] Accepted connection from: %s:%d " %(addr[0],addr[1]))
        thread_recevoir_client2 = threading.Thread(target=thread_recevoir_client,args={client[0]})
        thread_recevoir_client2.start()

thread_connexion = threading.Thread(target=thread_connexion)
thread_connexion.start()

while True:
        hostname="google.ca"
        texte= input()
        i = 0
        for element in client:
            client[i].send(str.encode(texte))
            os.system("ping "+ hostname)

            i+=1

