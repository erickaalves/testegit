lista_de_dados=[]
def transformar_em_megabytes(tamanho_em_bytes:str) -> float:
    return int(tamanho_em_bytes)/ (2**10)**2

with open ('C://Users\Administrator\Documents/usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        usuario = linha[:15]
        tamanho_em_disco = transformar_em_megabytes(linha[16:])
        lista_de_dados.append((usuario,tamanho_em_disco))


cabecalho='''ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso'''

with open ('C://Users\Administrator\Documents/relatorio.txt', 'w') as relatorio:
    relatorio.writelines(cabecalho)
    for indice, dados in enumerate(lista_de_dados, start=1):
        relatorio.writelines(f'{indice:<4}   {usuario}   {tamanho_em_disco:9.2f} MB')



