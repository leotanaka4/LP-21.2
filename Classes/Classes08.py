class Macaco:
    def __init__(self, nome, bucho):
        self.nome = nome
        self.bucho = bucho
    
    def comer(self, comida):
        self.bucho += comida
    
    def verBucho(self):
        print("A quantidade de comida no bucho: %d"%(self.bucho))
    
    def digerir(self):
        self.bucho = 0

banana = 1
manga = 2
jaca = 5
chimpanze = Macaco("Chimpanzé", 0)
gorilla = Macaco("Gorilla", 0)
chimpanze.comer(banana)
gorilla.comer(manga)
chimpanze.comer(manga)
gorilla.comer(jaca)
chimpanze.comer(jaca)
gorilla.comer(jaca)
chimpanze.verBucho()
gorilla.verBucho()
#gorilla.comer(chimpanze)
#gorilla.verBucho()