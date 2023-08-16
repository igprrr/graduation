from conta import Conta
class Banco:
    def __init__(self, numero, nome):
        self._numero = numero
        self._nome = nome
        self._vetContas = []