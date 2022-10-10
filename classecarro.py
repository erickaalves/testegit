class Carro:
    def __init__(self, ConsumoCarro, QuantidadeNoTanque:float = 0):
        self.QuantidadeNoTanque = QuantidadeNoTanque
        if self.QuantidadeNoTanque <= 0:
            print(f'O carro está sem gasolina, reabasteça')
        self.ConsumoCarro = ConsumoCarro

    def Andar(self, distancia):
            andara = distancia / self.ConsumoCarro
            print(f'Andarei {distancia:.2f} kms com {andara:.2f} litros')

    def AddGasolina(self, QuantosLitros):
        print(f'A quantidade de litros era {self.QuantidadeNoTanque}')
        self.QuantidadeNoTanque += QuantosLitros
        print(f'A quantidade de litros atual é de {self.QuantidadeNoTanque}')

    def RestaNoTanque(self, kmsPercorridos):
        if self.QuantidadeNoTanque <=0:
            print('O tanque está vazio')
        else:
            litros = kmsPercorridos / self.ConsumoCarro
            print(f'Resta no tanque {self.QuantidadeNoTanque - litros:.2f} litros')

MeuFusca = Carro (14)
MeuFusca.AddGasolina(40)
print(f'Esse carro faz {MeuFusca.ConsumoCarro} kms por litro')
MeuFusca.Andar(100)
MeuFusca.RestaNoTanque(40)