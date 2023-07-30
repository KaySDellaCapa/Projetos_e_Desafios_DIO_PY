""" 
PROJETO SISTEMA BANCARIO

Fui contratado por um banco para desenvolver seu novo sistema.
Esse banco deseja modernizar suas operações e para isso escolheu a
linguagem Python. Para a primeira versão do sistema deve-se implementar
apenas 3 operações: depósito, saque e extrato.

OPERAÇÃO DE DEPÓSITO
Deve ser possivel depositar valores positivos para a minha conta bancária.
A V1 do projeto trabalha apenas com 1 usuario, dessa forma não precisamos
nos preocupar em identificar qual é o número da ag^ncia e conta bancária.
Todos os depósitos devem ser armazenados em uma variavel e exibida na operação
de extrato

OPERAÇÃO DE SAQUE
O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00
por saque. Caso o usuario não tenha saldo em conta, o sistema deve exibir uma
mensagem informando que não será possível sacar o dinheiro por falta de saldo.
Todos os saques devem ser armazenados em uma variavel e exibidos na operação de
saque.

OPERAÇÃO DE EXTRATO
Essa operação deve listar todos os depósitos e saques realizados na conta; No fim
da listagem deve ser exibido o saldo atual da conta. Os valores devem ser
exibidos utilizando o formado R$.
"""
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3


def menu():
    print("                 ")
    print("- MENU DO BANCO -")
    print("1) Depositar")
    print("2) Sacar")
    print("3) Extrato")
    print("Use o 0 para sair")
    print("                 ")

while True:
    menu()
    escolha = input("Digite o número da opção desejada: ")
    if escolha == "1":

        valor = float(input("Informe o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += (f"Depósito: R${valor:.2f}")
        else:
            print("Operação falhou. Valor inválido")

    elif escolha == "2":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUE 

        if excedeu_saldo:
            print("Operação falhou. Saldo insuficiente.")
        elif excedeu_limite:
            print("Operação falhou. Limite de saque excedido.")
        elif excedeu_saques:
            print("Operação falhou. Limite de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += (f"Saque: R${valor:.2f}")
            numero_saque += 1
        else:
            print("Operação falhou. Valor inválido.")

    elif escolha == "3":
        print("--- EXTRATO ---")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("---------------")

    elif escolha == "0":
        print("Saindo... Até logo! ")
        break

    else:
        print("Opção inválida. Digite uma opção válida. ")