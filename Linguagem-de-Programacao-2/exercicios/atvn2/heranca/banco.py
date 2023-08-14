class Banco:
    def __init__(self, numero, nome):
        self._numero = numero
        self._nome = nome

#(3)Crie um método atualizar_contas() na classe Banco que seja responsável por controlar a
#atualização de todas as contas bancárias e gere um relatório com o saldo anterior e saldo novo
#de cada uma das contas e o saldo total de todas as atualizações. Dica: Para o valor de
#_saldo_total ser atualizado corretamente, atualize todas as funções atualiza nas outras
#classes para retornarem o valor correto com return self._saldo.
class AtualizarContas:
    def __init__(self, taxa_media, saldo_total = 0):
        self._taxa_media = taxa_media
        self._saldo_total = saldo_total

    def roda(self, conta):
        print("Saldo da Conta: {}".format(conta._saldo))
        self._saldo_total += conta.atualiza(self._taxa_media)
        print("Saldo Final: {}".format(self._saldo_total))
