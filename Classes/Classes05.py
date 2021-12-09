class Conta:
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome
        self.saldo = 0
    
    def alterarNome(self, nome):
        self.nome = nome
    
    def depositar(self, deposito):
        self.saldo += deposito

    def sacar(self, saque):
        if (saque <= self.saldo):
            self.saldo -= saque
        else:
            print("Não foi possível sacar!")