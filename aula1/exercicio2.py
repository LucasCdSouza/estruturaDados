import random
from utils import popularListaArquivo
letras = 'abcdefghijklmnopqrstuvwxyz'

lista = []
n = int(input('quantos nomes quer gerar?'))
tamanhoPalavra = int(input('qual o tamanho da palavra a ser sorteada?'))
i = 0
while (i < n):
    palavra = ''
    for j in range(tamanhoPalavra):
        posicaoLetras = random.randint(0, len(letras)-1)
        palavra += letras[posicaoLetras]

    if(palavra not in lista):
        lista.append(palavra)
        i+=1

lista.sort()       
print(lista)
popularListaArquivo(lista, "nomes.txt")
print('palavra sorteada: ', palavra)