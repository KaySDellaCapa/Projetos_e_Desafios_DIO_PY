import socket #Chama a API
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e: # Nome do objeto de erro é "e"
        print("A conexão falhou.")
        print("Erro: {}".format(e)) #Vai exibir o erro nas chaves e formatar
        sys.exit()

    print("Socket criado com sucesso!") #Ao passar pelo try

    hostAlvo = input("Digite o host ou IP a ser conectado: ")
    portaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((hostAlvo, int(portaAlvo))) # Se transformou em int para aceitar
        print("Cliente TCP conectado com sucesso no host: " + hostAlvo + " e na porta: " + portaAlvo)
        s.shutdown(2) # 2 segundos para fechar
    except socket.error as e:
        print("Não foi possivel conectar no host: "+ hostAlvo + " - Porta: " +portaAlvo)
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__": #Se o nome for main, chama o main
    main()