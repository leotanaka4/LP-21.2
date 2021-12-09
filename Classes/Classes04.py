class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura #altura em centímetros
    
    def envelhecer(self, anos):
        self.idade += anos
        if (self.idade < 21):
            self.altura += 0.5
    
    def engordar(self, ganho):
        self.peso += ganho
    
    def emagrecer(self, perda):
        self.peso += perda
    
    def crescer(self, ganho):
        self.altura += ganho