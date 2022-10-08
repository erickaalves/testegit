class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def Envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
            self.idade += 1
    def Engordar(self):
        pass
    def Emagrecer(self):
        pass
    def Crescer(self):
        pass

erick = Pessoa('Erick', 2, 12, 80)
larissa = Pessoa('Larissa', 3, 20, 70)
for _ in range(22):
    erick.Envelhecer()
    larissa.Envelhecer()
    print(f'a idade de {erick.nome} é {erick.idade} anos. E sua altura é {erick.altura} cm')
    print(f'{larissa.nome} tem {larissa.idade} e {larissa.altura} cms')