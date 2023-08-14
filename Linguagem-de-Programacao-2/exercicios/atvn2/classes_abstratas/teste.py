from conta import ContaInvestimento

ci = ContaInvestimento('126', 'igor', 1000.0)
ci.deposita(1000.0)
ci.atualiza(0.01)
print(ci._saldo)