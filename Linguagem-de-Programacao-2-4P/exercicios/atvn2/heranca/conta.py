#(1)Adicione na classe conta um método chamado atualiza() para atualizar a conta de acordo com uma
#taxa percentual.

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa
        return self._saldo

#(2)Crie duas subclasses da classe Conta: ContaCorrente e ContaPoupanca. Ambas terão o
#método atualiza() reescrito: a ContaCorrente deve atualizar-se com o dobro da taxa e a
#ContaPoupanca deve atualizar-se com o triplo da taxa. Além disso, a ContaCorrente deve
#reescrever o método deposita() a fim de retirar uma taxa bancária de dez centavos de cada
#depósito'''

class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
        return self._saldo
        
class ContaCorrente(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
        return self._saldo

    def deposita(self, valor):
        self._saldo += valor - 0.10