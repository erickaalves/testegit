class Bomba_De_Combustivel:
    def __init__(self, TipoCombustivel:str, ValorLitro:float , QuantidadeCombustivel:float):
        self.TipoCombustivel = TipoCombustivel
        self.ValorLitro = ValorLitro
        self.QuantidadeCombustivel = QuantidadeCombustivel

    def AbastecerPorValor(self, valor:float):
        litros_abastecidos = valor / self.ValorLitro
        self._ApresentarInfo(litros_abastecidos, valor)

    def _ApresentarInfo(self,litros_abastecidos, valor):
        if litros_abastecidos > self.QuantidadeCombustivel:
            print(f'Nao e possivel abastecer, faltam {litros_abastecidos - self.QuantidadeCombustivel:.2f} litros')
            print('Reabasteça a Bomba')
        else:
            self.QuantidadeCombustivel -= litros_abastecidos
            print(f'Foram abastecidos {litros_abastecidos:.2f} litros ao valor de R$ {valor:.2f}')
            print(f'Sobraram na bomba {self.QuantidadeCombustivel:.2f} litros')

    def AbastecerPorLitro(self, litros_abastecidos:float):
        valor = litros_abastecidos * self.ValorLitro
        self._ApresentarInfo(litros_abastecidos, valor)

    def AlterarValor(self, valor:float):
        print(f'O valor do litro era de {self.ValorLitro:.2f}, o novo valor é de {valor:.2f}')
        self.valor = valor

    def AlterarQuantidadeCombustivel(self, nova_quantidade:float):
        if nova_quantidade >= 0:
            self.QuantidadeCombustivel += nova_quantidade
        else:
            print('Voce nao vai tirar gasolina daqui')

        print(f'O estoque estava em {self.QuantidadeCombustivel:.2f} lts e agora esta com {nova_quantidade:.2f} lts')
        self.QuantidadeCombustivel = nova_quantidade

bomba=Bomba_De_Combustivel('Gasolina', 4.59, 100.0)

bomba.AbastecerPorLitro(10)
bomba.AbastecerPorValor(100)
bomba.AlterarValor(5)
bomba.AbastecerPorLitro(70)
