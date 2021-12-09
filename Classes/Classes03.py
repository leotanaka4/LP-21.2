class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.area = self.ladoA*self.ladoB
        self.perimetro = 2*self.ladoA + 2*self.ladoB

    def mudaLados(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.area = ladoA*ladoB
        self.perimetro = 2*ladoA + 2*ladoB
    
    def retornaLadoA(self):
        return self.ladoA
    
    def retornaLadoB(self):
        return self.ladoB
    
    def calculaArea(self):
        self.area = self.ladoA*self.ladoB
        return self.area
    
    def calculaPerimetro(self):
        self.perimetro = 2*self.ladoA + 2*self.ladoB
        return self.perimetro

a = float(input(print("Digite o primeiro lado:")))
b = float(input(print("Digite o segundo lado:")))
objeto = Retangulo(a, b)
if (objeto.area % 2 == 0):
    pisos = objeto.area//2 #pisos de 2 m²
else:
    pisos = objeto.area//2 + 1
if (objeto.perimetro % 4 == 0):
    rodapes = objeto.perimetro//4 #rodapés de 4 m
else:
    rodapes = objeto.perimetro//4 + 1
print("Quantidade de pisos: %d"%(pisos))
print("Quantidade de rodapés: %d"%(rodapes))