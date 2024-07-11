import socket

HOST = '192.168.2.245'
PORT = 50000
name=str(input("Digite o seu nome"))
server = (HOST, PORT)

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input(f'Message to {HOST}: \n')
    msg = msg.encode('utf-8')
    name=name.encode("utf-8")
    udpSocket.sendto(msg,name, server)
    data, server = udpSocket.recvfrom(512)
    if data:
        data = data.decode('utf-8')
        print(data)
udpSocket.close()