import socket
import threading

serveur_ip = "192.168.60.230"
serveur_port = 8118

#def thread_recevoir(client_socket):
    #while True:
    #    response = client.recv(1024)
    #    print(response)

def thread_ping():
    import os
    hostname = serveur_ip

    #if response == 0:
    #    print(hostname, 'is up!')
    #else:
    #    print(hostname, 'is down!')

    while True:
        response = client.recv(1024)
        print(response[0])
        os.system("ping " + str(response[0:len(response)-1]))


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((serveur_ip, serveur_port))

thread_ping = threading.Thread(target=thread_ping, args={})
thread_ping.start()

while True:
    texte = input()
    client.send(str.encode(texte))

#x = 1
#while x is not 9:
#    thread_ping()
#    x += 1

