"""
1. Um cliente pede ao servidor uma transação a validar;
a. Se existem transações, o servidor envia a transação, o número de
bits zero esperado, o número de clientes já validando essa
transação e a janela de validação;

2. O cliente tenta sucessivamente encontrar o nonce dentro da janela de
validação, concatenando um valor de quatro bytes big-endian no início da
transação;
3. Se o número de bits zero é encontrado, o nonce é informado ao servidor;
"""
import socket
Port=31471

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)