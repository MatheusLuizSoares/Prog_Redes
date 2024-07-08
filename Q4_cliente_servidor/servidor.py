import socket

HOST=''
PORT=5000

udp_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((HOST,PORT))

print("Recebendo mensagens...\n\n")


while True:
        msg,cliente=udp_socket.recvfrom(512)


        print(cliente,msg.decode('utf-8'))

        
        udp_socket.close()