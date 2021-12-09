class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.tanque = 0
    
    def andar(self, distancia):
        gasto = distancia/self.consumo
        if (gasto <= self.tanque):
            self.tanque -= gasto
        else:
            print("O tanque ficou vazio antes de você chegar ao seu destino!")
    
    def obterGasolina(self):
        return self.tanque

    def adicionarGasolina(self, litros):
        self.tanque += litros

meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.