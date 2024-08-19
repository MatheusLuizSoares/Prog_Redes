import threading

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def processa_numero(num):
    if eh_primo(num):
        print(f"{num} é primo")
    else:
        print(f"{num} não é primo")

limite = int(input("Digite o número limite: "))
therds = int(input("Digite o número de threads:"))

for num in range(2, limite + 1):
    therds_atuais = threading.Thread(target=processa_numero, args=(num,))
    therds_atuais.start()
    therds_atuais.join()

print("Todas as threads foram processadas.")
