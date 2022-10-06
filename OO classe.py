class Carro:
    ##tres propriedades
    def __init__(self, cor, ano, modelo):
        self.cor = cor
        self.ano = ano
        self.modelo = modelo
    def ligar(self):
        print('Estou ligando')
    def desligar(self):
        print('Estou deligando')
    def infocar(self):
        print(self.cor, self.ano, self.modelo)
carro1= Carro('ford', '2009', 'hatch')
##tem tres metodos def, ligar, desligar e infocar...

carro1.ligar()
carro1.desligar()
carro1.infocar()

##chamando as funções criadas acima.