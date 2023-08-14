from conta import ContaCorrente, SeguroDeVida
from manipulador import ManipuladorDeTributaveis

cc1 = ContaCorrente('123', 'igor', 900, 1200)
cc2 = ContaCorrente('123', 'ellem', 1000, 1250)
seguro1 = SeguroDeVida(150, 'igor melo', '22334')
seguro2 = SeguroDeVida(230, 'ellem jady', '55667')

lista_tributaveis = []
lista_tributaveis.append(cc1)
lista_tributaveis.append(cc2)
lista_tributaveis.append(seguro1)
lista_tributaveis.append(seguro2)

manipulador = ManipuladorDeTributaveis()
total = manipulador.calcula_impostos(lista_tributaveis)
print(total)
