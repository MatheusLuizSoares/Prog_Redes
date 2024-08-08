import sys
import socket

try:
    request= sys.argv[1]
    protocolo= request.split(':',1)[0]
    nome_arquivo=request.split("/",4)[1]
    if len (sys.argv)>2:
        arquename=str(sys.argv[2])
except Exception as exc:


try:
    if protocolo=="http" :
     
     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except Exception as exc:
