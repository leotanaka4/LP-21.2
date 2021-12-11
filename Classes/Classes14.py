class Funcionario:
    def __init__(self, nome, salario):
        self.nome = str(nome)
        self.salario = float(salario)
    
    def devolverNome(self):
        return self.nome
    
    def devolverSalario(self):
        return self.salario
    
    def aumentarSalario(self, porcentualDeAumento):
        self.salario *= 1+(porcentualDeAumento/100)

harry = Funcionario("Harry", 25000)
harry.aumentarSalario(10)
print("Novo salário: R$ %.2f"%(harry.salario))