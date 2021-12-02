class Contato:
    def __init__(self,nome,tel,end):
        self.nome = nome
        self.tel = tel
        self.end = end
    
    def get_nome(self):
        return self.nome
    
    def get_tel(self):
        return self.tel
    
    def get_end(self):
        return self.end
    
    def digitar(self):
        print(self.nome+"/"+self.tel+"/"+self.end)

