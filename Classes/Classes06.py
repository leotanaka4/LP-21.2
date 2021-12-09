class Tv:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume
    
    def retornaCanal(self):
        return self.canal
    
    def mudaVolume(self, alteração):
        if (self.volume + alteração >= 0 and self.volume + alteração <=100):
            self.volume += alteração
        else:
            print("Não foi possível alterar o volume!")