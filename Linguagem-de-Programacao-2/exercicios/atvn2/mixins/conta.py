class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
#(7)O banco precisa tributar dinheiro de alguns bens que nossos clientes possuem. Para isso, crie
#uma classe Tributavel com um método que devolve o imposto sobre a conta.

class Tributavel:
    def get_valor_imposto(self):
        pass

#(8)Transforme a classe Tributavel em um mix-in e faça a classe ContaCorrente herdar da
#classe TributavelMixIn e implemente o método "exigido" pelo MixIn.

class TributavelMixIn:
    def get_valor_imposto(self):
        pass

class ContaCorrente(Conta, TributavelMixIn):
    def get_valor_imposto(self):
        return self._saldo * 0.01
    
#9. Alguns recursos são tributáveis e outros não. Por exemplo: ContaPoupanca não é tributável,
#já para ContaCorrente você precisa pagar 1% da conta e o SeguroDeVida tem uma faixa fixa
#de 50 reais mais 5% do valor do seguro. Crie a classe SeguroDeVida que vai herdar de
#TributavelMixIn. Crie seus respectivos atributos e implemente o método do MixIn.
class SeguroDeVida(TributavelMixIn):
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05