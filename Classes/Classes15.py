class Tamagushi:
    def __init__(self, nome, fome, saude, idade, tedio):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.tedio = tedio
    
    def alterar(self, desejado, info):
        if (desejado == "Nome"):
            self.nome = info
        elif (desejado == "Fome"):
            self.fome = info
        elif (desejado == "Saúde"):
            self.saude = info
        elif (desejado == "Idade"):
            self.idade = info
        else:
            print("Essa mudança não existe!")
    
    def retornar(self, desejado):
        if (desejado == "Nome"):
            return self.nome
        elif (desejado == "Fome"):
            return self.fome
        elif (desejado == "Saúde"):
            return self.saude
        elif (desejado == "Idade"):
            return self.idade
        else:
            print("Esse atributo não existe!")
    
    def retornarHumor(self):
        humor = self.fome + self.saude
        return humor
    
    def alimentar(self, comida):
        self.fome -= comida
    
    def brincar(self, brincadeira):
        self.tedio -= brincadeira