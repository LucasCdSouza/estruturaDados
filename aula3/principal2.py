from glicemia import glicemia

lista_glicemica = []
nome_arquivo = './glicemia.txt'

with open(nome_arquivo, 'r', encoding='utf8') as leitor:
    for linha in leitor:
        valor, data, hora = linha split (',')
        objeto = Glicemia(valor, data, hora)
        if obeto not in lista_glicemica:
            lista_glicemica.append ( objeto)

print('Quantidade de dados lidos', len(lista_glicemica)