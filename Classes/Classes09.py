class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def imprimir(self):
        print("Posição x = %d e posição y = %d."%(self.x, self.y))

class Retangulo(Ponto):
    def __init__(self, x, y, largura, altura):
        self.vertice = Ponto(x, y)
        self.largura = largura
        self.altura = altura

    def encontrarCentro(self):
        self.centro = Ponto(self.vertice.x + self.largura/2, self.vertica.y + self.altura/2)
        print("Centro na posição x = %.2f e y = %.2f"%(self.centro.x, self.centro.y))
        return self.centro

vertice = Ponto(0,0)
vertice.x = float(input(print("Digite a posição do eixo x do retângulo: ")))
vertice.y = float(input(print("Digite a posição do eixo y do retângulo: ")))
largura = float(input(print("Digite a largura do retângulo: ")))
altura = float(input(print("Digite a altura do retângulo: ")))
retangulo = Retangulo(vertice.x, vertice.y, largura, altura)
centro = retangulo.encontrarCentro()