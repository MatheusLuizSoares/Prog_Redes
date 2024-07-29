import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)




sock.connect(("httpbin.org", 80))
sock.send (b"GET  /image/jpeg HTTP/1.1\r\n"+
           b"Host: httpbin.org\r\n"+
           b"\r\n")

data = sock.recv(4096)

metadados, dados = data.split (b"\r\n\r\n")

for metadado in metadados.split(b"\r\n"):
    print (metadado)
    dadosMeta = metadado.split(b":")
    if dadosMeta[0] == b"Content-Length":
        tamEsperado = int(dadosMeta[1])
        print (tamEsperado)

metadados=(dados+2)


fd = open("x.bin", "wb")
fd.write(data)
fd.close()

sock.close()