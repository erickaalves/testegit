class Bola:
##atributos
    def __init__(self):
        self.cor = "Azul"
        self.circuferencia = '10cm'
        self.materia = 'Plástico'
##atributos

##metodos
    def mostra_cor(self):
        return id(self)
    def troca_cor (self, cor):
        self.cor = cor
##metodos

circulo_1 = Bola()
circulo_2 = Bola()

circulo_1.troca_cor('Amarelo')

print(type(circulo_1))
print(circulo_1 is circulo_2)
##circulo_1.mostra_cor está assim pq mandamos retornar o id de self (do próprio objeto circulo_1)

print(circulo_1.mostra_cor(), id(circulo_1))
print(circulo_2.cor)
print(circulo_1.cor)
