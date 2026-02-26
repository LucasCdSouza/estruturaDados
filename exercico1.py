#popular uma lista 
import random
from utils import popularListaArquivo

lista = []

n = int(input("Quantos elementos deseja gerar? "))

i = 0
while(i < n):
    numeroSorteado = random.randint(0, 1000000)
    if(numeroSorteado not in lista):
        lista.append(numeroSorteado)
        i+=1

lista.sort()
print("total de elementos: ", len(lista))
#print(lista)
popularListaArquivo(lista, "numeros.txt")