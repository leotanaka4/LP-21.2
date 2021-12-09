class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocaCor(self, cor):
        self.cor = cor
    
    def mostraCor(self):
        return self.cor
    
a = Bola("Laranja", 30, "Plástico")
print(a.mostraCor())
nova = str(input(print("Digite a nova cor: ")))
a.trocaCor(nova)
print("Nova cor: "+a.cor)