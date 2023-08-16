from conta import Conta, ContaCorrente, ContaPoupanca

#dados da c, cc e cp
c = Conta('123', 'igor', 1000, 3000.0)
cc = ContaCorrente('124', 'igor melo', 2000, 4000)
cp = ContaPoupanca('125', 'igor melo de sousa', 4000, 6000)

c.atualiza(0.01)
cc.atualiza(0.01)
cp.atualiza(0.01)

print('o saldo da conta de Igor é:',c._saldo)
print('o saldo da conta corrente é:',cc._saldo)
print('o saldo da conta poupança é:',cp._saldo)
