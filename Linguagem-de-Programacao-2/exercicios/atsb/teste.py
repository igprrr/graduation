import math
from datetime import date
from cliente import Cliente

#classe do banco que faz transferencia
class Banco:
    def transferencia(conta,contas):
        transferir = int(input("insira o numero da conta para transferir: ")) 
        quantidade = int(input("insira quanto quer transferir: "))
        try:
            if conta.saldo_disponivel(quantidade):
                contas[transferir].deposito(quantidade)
                conta.saca(quantidade)
            else:
                print("Error")
        except KeyError:
            print("Error: conta não encontrada")
#classe para validar data de validade das contas para comparar as datas e ver se é possível fazer transferência
def validar_data(data):
    mes = 0
    ano = 0
    temp = math.trunc(data / 1000)
    r1 = data % 1000
    mes += temp * 10
    temp = math.trunc(r1 / 100)
    mes += temp
    r1 = r1 % 100
    temp = math.trunc(r1 / 10)
    ano += temp * 10
    r1 = r1 % 10
    ano += r1
    data_atual = today.strftime("%m/%y")
    lista_dia = data_atual.split('/') 
    mes_t = int(lista_dia[0])
    ano_t = int(lista_dia[1])
    if ((ano_t > ano) or (mes_t > mes and ano_t == ano)):
        return False
    else:
        return True
#execução do programa
s = 1
contas =  {}
today = date.today()
while s == 1:
    print("O que deseja fazer? \n1. criar conta \n2. transferir para a conta \n3. eliminar conta \n4. mostrar conta\n")
    resp = int(input())
    if resp == 1:
        Cliente.criarconta(contas)
    elif resp == 2:
        transfer_a = int(input("insira o numero da conta de onde transferir: "))
        if validar_data(contas[transfer_a].vencimento):
            try:
                Banco.transferencia(contas[transfer_a],contas)
            except KeyError:
                print("Error: conta não existente")
        else:
            print("conta já vencida")
    elif resp == 3:
        apag = int(input("insira o numero da conta: "))
        print('conta apagada!')
        Cliente.apagar_conta(contas, apag)
        
    elif resp == 4:
        Cliente.mostrar_conta(contas)
    else:
        print("opção não válida")
s = int(input("deseja fazer outra ação? \n 1. sim \n 2. não \n"))
