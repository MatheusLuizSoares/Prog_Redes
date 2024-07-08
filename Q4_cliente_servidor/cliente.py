import socket

HOST='10.25.3.161'
PORT=5000

udp_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:

  
    msg=input("Digite uma mensagem:")
    msg=msg.encode("utf-8")
    udp_socket.sendto(msg,(HOST,PORT))

    udp_socket.close()