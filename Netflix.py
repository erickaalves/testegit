class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
    ##self.lista_de_planos e lista_de planos tem diferença.
    ##self.lista_de_planos a gente usa em todas as funções.
        self.lista_de_planos = ["basic","premium"]
        self.plano = plano
        if plano in self.lista_de_planos:
            self.plano = plano
        else:
            raise Exception('Plano Inválido')
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_de_planos:
            self.plano = novo_plano
        else:
            print('Plano Inválido')

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme {filme}')
        elif self.plano == 'premium':
            print(f'Ver filme {filme}')
        elif self.plano == "basic" and plano_filme == "premium":
            print('Faça upgrade pra ver esse filme')
        else:
            print('Plano Inválido')


cliente=Cliente('Lira', 'erickdosantos53@gmail.com', 'basic')
print(cliente.plano)
cliente.ver_filme('Harry Potter', 'premium')
##upgrade de plano
cliente.mudar_plano("premium")
print(cliente.plano)