import random

class Bichinho:
    def __init__(self, nome, saude, idade):
        self.nome = nome
        self.saude = saude
        self.idade = idade
        self.fome = random.randrange(1, 101)
        self.tedio = random.randrange(1, 101)

def Alimentar(lista):
    j = 0
    for i in lista:
        lista[j].fome -= 10

def Brincar(lista):
    j = 0
    for i in lista:
        lista[j].tedio -= 10
        lista[j].fome -= 10
        lista[j].saude += 10

def Ouvir(lista):
    j = 0
    for i in lista:
        print("Au Au! Miau Miau!")

fazenda = [Bichinho("Dory", 100, 1), Bichinho("Fafa", 100, 3)]

comando = 0

while (comando != "FIM"):
    a = input("Digite Alimentar/Brincar/Ouvir/FIM \n")
    if (a == "Alimentar"):
        Alimentar(fazenda)
        pass
    elif(a == "Brincar"):
        Brincar(fazenda)
        pass
    elif(a == "Ouvir"):
        Ouvir(fazenda)
        pass
    elif(a == "FIM"):
        comando = a
    else:
        print("Essa opção não existe")