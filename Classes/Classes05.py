class Conta:
    def __init__(self, numero, nome, saldo):
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

a = Conta(123, "Leonardo", 0)
a.depositar(200)
print(a.saldo)
a.sacar(50)
print(a.saldo)
a.sacar(200)