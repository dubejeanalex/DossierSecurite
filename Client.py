import socket
import threading

serveur_ip = "192.168.60.230"
serveur_port = 8118

def thread_recevoir(client_socket):
    while True:
        response = client.recv(1024)
        print(response)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((serveur_ip,serveur_port))

thread_recevoir =  threading.Thread(target=thread_recevoir, args={client,})

thread_recevoir.start()

while True:
    texte = input()
    client.send(str.encode(texte))