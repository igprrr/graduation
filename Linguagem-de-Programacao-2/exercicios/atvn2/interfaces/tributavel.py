#(11)Torne Tributavel uma classe abstrata e o método get_valor_imposto() abstrato.
class Tributavel:
    def get_valor_imposto(self):
        pass

#(12)Nada impede que os usuários da classe Tributavel implementem o método
#get_valor_imposto de maneira não esperada. Então, acrescente a documentação utilizando
#docstring e utilize a função help() para acessar a documentação:
import abc
class Tributavel(abc.ABC):
    @abc.abstractmethod
    def get_valor_imposto(self):
        pass 

#(14)Modifique o método calcula_impostos() da classe ManipuladorDeTributaveis para
#checar se os elementos da listas são tributáveis através do método isinstance(). Caso um
#objeto da lista não seja um tributável, imprimir uma mensagem de erro e apenas os tributáveis
#serão somados ao total.

class ManipuladorDeTributaveis:
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            if (isinstance(t, Tributavel)):
                total += t.get_valor_imposto()
            else:
                print("não é um tributável")    
        return total    

class SeguroDeVida(Tributavel):
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05