class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def trocaLado(self, lado):
        self.lado = lado
    
    def retornaLado(self):
        return self.lado
    
    def calculaArea(self):
        area =  self.lado**2
        return area