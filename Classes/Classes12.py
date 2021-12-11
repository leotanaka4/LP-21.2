class contaInvestimento:
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome
        self.saldo = 0
        self.taxaJuros = 0
    
    def configurar(self, saldo, taxaJuros):
        self.saldo = saldo
        self.taxaJuros = taxaJuros
    
    def adicioneJuros(self):
        self.saldo *= 1+self.taxaJuros

poupança = contaInvestimento(123, "Leonardo")
poupança.configurar(1000, 0.10)
poupança.adicioneJuros()
poupança.adicioneJuros()
poupança.adicioneJuros()
poupança.adicioneJuros()
poupança.adicioneJuros()
print("Saldo da conta: R$ %.2f"%(poupança.saldo))