class bombaComustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    
    def abastecerPorValor(self, valor):
        litro = valor/self.valorLitro
        if (litro <= self.quantidadeCombustivel):
            self.quantidadeCombustivel -= litro
            print("Volume de combústivel abastecido = %.2f L"%(litro))
        else:
            print("Não é possível abastecer essa quantidade de combústivel!")

    def abastecerPorLitro(self, litros):
        valor = litros*self.valorLitro
        if (litros <= self.quantidadeCombustivel):
            self.quantidadeCombustivel -= litros
            print("Valor gosto no abastecimento: R$ %.2f"%(valor))
        else:
            print("Não é possível abastecer essa quantidade de combustível!")
    
    def alteraValor(self, valorLitro):
        self.valorLitro = valorLitro
    
    def alterarQuantidadeCombustivel(self, novaQuantidadeCombustivel):
        self.quantidadeCombustivel = novaQuantidadeCombustivel