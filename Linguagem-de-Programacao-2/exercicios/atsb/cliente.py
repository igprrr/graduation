from conta import Conta
#criar conta
class Cliente:
    def criarconta(contas):
        nome = input('insira o nome: ')
        numero = int(input('insira o numero da conta: '))
        cpf = input('insira o seu cpf: ')
        vencimento = int(input('insira o ano de vencimento da conta: '))
        saldo_inicial = int(input('insira o saldo inicial: '))
        nova = Conta(nome, numero, cpf, vencimento, saldo_inicial)
        contas[numero] = nova
    def apagar_conta(contas, numero):
        try:
            del(contas[numero])
        except KeyError:
            print("Error: conta não existente: ")

    def mostrar_conta(contas):
        numero = int(input("insira o numero da conta: "))
        try:
            print(contas[numero])
        except KeyError:
            print("Error conta não existente")