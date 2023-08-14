from tributavel import Tributavel
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

class ContaCorrente(Conta, Tributavel):
    def get_valor_imposto(self):
        return self._saldo * 0.01

    def deposita(self, valor):
        self._saldo += valor - 0.10
        return self._saldo
        
class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
        return self._saldo
        
#(15)A ContaInvestimento também deve ser um tributável, cobrando 3% do saldo. Registre a
#classe ContaInvestimento como tributável. Adicione a ContaInvestimento criada na lista
#de tributáveis e calcule o total de impostos através do ManipuladorDeTributaveis.
class ContaInvestimento(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5
        return self._saldo

    def get_valor_imposto(self):
        return self._saldo * 0.03

#(13)Faça com que ContaCorrente e SeguroDeVida não mais herdem da classe
#Tributavel. Então registre as classes ContaCorrente e SeguroDeVida como subclasses
#virtuais de Tributavel , de modo que funcione como uma interface.

class ContaCorrente(Conta):
    pass

class SeguroDeVida:
    pass