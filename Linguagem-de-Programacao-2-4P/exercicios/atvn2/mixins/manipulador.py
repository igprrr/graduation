#10. Crie a classe ManipuladorDeTributaveis em um arquivo chamado manipulador.py. Essa
#classe deve ter um método chamado calcula_impostos() que recebe uma lista de tributáveis e
#retorna o total de impostos cobrados:
class ManipuladorDeTributaveis:

    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            total += t.get_valor_imposto()
        return total    