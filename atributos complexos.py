class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}'

pessoa1 = Pessoa(nome='Erick')

pai1 = Pessoa(('Erick', 'Carol', 'Sara'), nome = 'Roberto', idade = 40)
print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.cumprimentar())
print(pai1.filhos)