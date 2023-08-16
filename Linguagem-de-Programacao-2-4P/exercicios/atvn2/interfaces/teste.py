from tributavel import ManipuladorDeTributaveis, SeguroDeVida
from conta import ContaPoupanca, ContaCorrente
from tributavel import ManipuladorDeTributaveis

cc = ContaCorrente('1234', 'Igor', 1400, 2000)
seguro = SeguroDeVida(230, 'igor melo', 1557)

lista_tributaveis = []
lista_tributaveis.append(cc)
lista_tributaveis.append(seguro)
mt = ManipuladorDeTributaveis()
total = mt.calcula_impostos(lista_tributaveis)
print(total)
cp = ContaPoupanca('1236', 'ellem jady', 1800, 3000)
lista_tributaveis.append(cp)
