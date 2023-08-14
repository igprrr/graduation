#5. Transforme a classe Conta em uma classe abstrata e o método atualiza() em um método
#abstrato.

import abc
class Conta(abc.ABC):
    def __init__(self, numero, titular, saldo = 0, limite = 3000):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    @abc.abstractmethod
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa
        return self._saldo

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

#6. Crie uma classe ContaInvestimento. O que deve ser feito para instanciar um objeto dessa
#classe?
class ContaInvestimento(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5
        return self._saldo
    def deposita(self, valor):
        self._saldo += valor - 0.10
        return self._saldo