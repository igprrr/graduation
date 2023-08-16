class Conta:
    __dinheiro = 0
    def __init__(self,nome,numero, cpf, vencimento,dinheiro):
        self.nome = nome
        self.__numero = numero
        self.__cpf = cpf
        self.vencimento = vencimento
        self.__dinheiro = dinheiro

    #definir os dados e mostrar na sequencia 
    def __str__(self):
        return "Nome do titular: {} \n numero: {} \n cpf: {} \n ano de vencimento: {} \n saldo: {} ".format(self.nome,self.__numero,self.__cpf, self.vencimento,self.__dinheiro)

   #funçao deposito na conta
    def deposito(self,valor):
        self.__dinheiro += valor
        print("saldo atual é de: ",self.__dinheiro)

    #funçao que checa o saldo disponivel
    def saldo_disponivel(self,valor):
        if self.__dinheiro >= valor:
            return True
        else:
            return False

    #realiza o saque da conta
    def saca(self,valor):
        if valor > self.__dinheiro: #Valida que tenga fondos suficientes
            print("nao tem saldo suficente para a ação")
        else:
            self.__dinheiro -= valor
            print("saldo atual da conta {} é de: {}  ".format(self.__numero,self.__dinheiro))