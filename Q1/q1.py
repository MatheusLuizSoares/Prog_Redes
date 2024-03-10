# Criando os parâmetros
nome_arq_ori = input("Digite o nome do arquivo de origem: ")
palavra_passe = input("Digite uma palavra-passe: ")
nome_arq_dest = input("Digite o nome do arquivo de destino: ")

# criando um try
try:
  # Abrindo o arquivo no modo binário
  with open(nome_arq_ori, "rb") as file_origem:
        dado_ori = file_origem.read()

    
  try:
    with open(nome_arq_dest, "xb") as file_destino:
      pass
  # Criando um except para que não haja arquivo repetido
  except FileExistsError:
        print("O arquivo já existe. Escolha um novo nome.")
  else:
    #vai saber o tamanho
     tam_palavra_passe = len(palavra_passe)
     
       # Um bytearray é um metodo semelhante a uma lista, mas é mutável, permitindo a modificação dos valores dos bytes.
     dado_cript = bytearray()
     
    #O for vai ser criado para que obtenha tanto os valores de i e do byte,por isso o uso do enumemerate
     for i, byte in enumerate(dado_ori):
            byte_palavra_passe = ord(palavra_passe[i % tam_palavra_passe])
            byte_cripto = byte ^ byte_palavra_passe
            dado_cript.append(byte_cripto)
     #a gente vai modificar o arquivo por isso ouso "wb"
     with open(nome_arq_dest, "wb") as file_destino:
            file_destino.write(dado_cript)
            print("A criptografia foi concluída com sucesso")

except FileNotFoundError:
    print("Arquivo de origem não encontrado")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
#finalizando o codigo
#o codigo pode ser visto atraves do 