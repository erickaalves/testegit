class Quadrado:
    def __init__(self, lado=1):
        self.lado = lado
    def calc_area(self):
        return self.lado ** 2

quadrado = Quadrado(4)

print(f'O lado do quadrado é {quadrado.lado}')
print(f'A area do quadrado é {quadrado.calc_area()}')