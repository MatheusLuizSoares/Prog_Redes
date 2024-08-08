import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)




sock.connect(("httpbin.org", 80))
sock.send (b"GET  /image/jpeg HTTP/1.1\r\n"+
           b"Host: httpbin.org\r\n"+
           b"\r\n")

data = sock.recv(1200)
tamEsperado=0

pos2NL=data.find(b"\r\n\r\n")
while pos2NL==-1:
    data+=sock.recv(1200)
    pos2NL= data.find(b"\r\n\r\n")
metadados, dados = data.split (b"\r\n\r\n")
for metadado in metadados.split(b"\r\n"):
    print()

metadados=dados.decode(dados+2)
metadados1=metadados("UTF-8")


fd = open("x.bin", "wb")
fd.write(data)
fd.close()

sock.close()
