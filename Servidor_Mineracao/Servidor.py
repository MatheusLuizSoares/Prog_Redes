"""
1. O servidor pede sucessivamente transações ao usuário (e os bits zero
esperados) e as armazena; o usuário pode demorar a responder, então isso
não deve travar o processamento de transações já informadas antes;
2. O servidor atende pedidos de agentes/clientes por de transações a validar
e retorna a eles uma transação, o número de bits zero esperado, o número
de clientes já validando a transação e o tamanho da janela de validação
definida no programa (exemplo, se a janela for 1000000, espera-se que o
cliente 0, tente encontrar o nonce entre 0 e 999999, o cliente 1 de 1000000
a 1999999 e assim por diante);
3. Enquanto uma transação ainda não foi validada, o servidor a envia a todos
os agentes que solicitarem;
4. Se não existem transações a validar, o servidor informa essa condição aos
clientes que solicitarem.
"""

"""(PARTE 2)
1. O servidor ao receber a notificação de um cliente de que encontrou o
nonce, verifica se este é realmente válido (o processo de validação deve
ser executado para um cliente por vez, para evitar condições de corrida que
geram erro):
a. Se o nonce é válido, todos os clientes são notificados pelo servidor
para que parem o procedimento de mineração vigente; o vencedor
é notificado de forma diferente, indicando o seu sucesso;
b. Se o nonce é falso, o servidor notifica apenas cliente que o
encontrou, indicando tratar-se de valor inválido.
"""
import socket, sys, os
Host=31471


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


nance=0