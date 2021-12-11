class Funcionario:
    def __init__(self, nome, salario):
        self.nome = str(nome)
        self.salario = float(salario)
    
    def devolverNome(self):
        return self.nome
    
    def devolverSalario(self):
        return self.salario
    
empregado = Funcionario("Leonardo", 1250)
nome = empregado.devolverNome()
salario = empregado.devolverSalario()
print("Funcionário '%s' ganha %.2f reais!"%(nome, salario))